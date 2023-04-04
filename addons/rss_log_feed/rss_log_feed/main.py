"""Custom addon to listen to the YAS-209 and post updates to HA"""
from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from json import JSONDecodeError, dumps, loads
from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING, LogRecord, getLogger
from os import environ, getenv
from traceback import format_exc
from typing import Any

from dotenv import load_dotenv
from feedgen.feed import FeedGenerator
from flask import Flask, Request, Response, make_response, request
from paramiko import AutoAddPolicy, SFTPClient, SSHClient
from pydantic import BaseModel, Extra, ValidationError
from wg_utilities.exceptions import on_exception
from wg_utilities.functions import force_mkdir, user_data_dir
from wg_utilities.loggers import add_list_handler, add_stream_handler

load_dotenv()

LOGGER = getLogger(__name__)
LOGGER.setLevel(DEBUG)
add_stream_handler(LOGGER)

RECORD_COLLECTOR = getLogger("RecordCollector")
RECORD_COLLECTOR.setLevel(DEBUG)

app = Flask(__name__)

_LOG_TTL = (
    3 * 24 * 60 * 60
    # Need the `or` here in case the env var is `None` for some reason
    if (log_ttl := (getenv("LOG_TTL") or "null").lower()) == "null"
    else int(log_ttl)
)

LOGGER.debug("`log_ttl` is %s", log_ttl)

LH = add_list_handler(RECORD_COLLECTOR, log_ttl=_LOG_TTL)

NAME_TO_LEVEL = {
    "CRITICAL": CRITICAL,
    "ERROR": ERROR,
    "WARN": WARNING,
    "WARNING": WARNING,
    "INFO": INFO,
    "DEBUG": DEBUG,
}

NAME_TO_RECORD_LIST = {
    "CRITICAL": LH.critical_records,
    "ERROR": LH.error_records,
    "WARNING": LH.warning_records,
    "INFO": LH.info_records,
    "DEBUG": LH.debug_records,
}

LOCAL_TZ = datetime.now().astimezone().tzinfo
SFTP_LOG_PATH = "/config/.addons/rss_log_feed"


class LogPayload(BaseModel, extra=Extra.allow):
    """Model for the payload data"""

    client: str
    message: str
    extra: Mapping[str, Any]

    @classmethod
    def from_request(cls, req: Request) -> LogPayload:
        """

        Args:
            req (Request): the inbound request

        Returns:
            LogPayload: model instance containing request info
        """
        log_payload = {}

        raw_payload = {}
        if req.is_json:
            raw_payload = req.json
            log_payload["message"] = raw_payload.pop("message", None)
        else:
            try:
                # In case it's stringified JSON
                raw_payload = loads(req.data.decode())
                log_payload["message"] = raw_payload.pop("message", None)
            except JSONDecodeError:
                log_payload["message"] = req.data.decode()

        log_payload["client"] = (
            req.remote_addr
            if (client := raw_payload.pop("client", None)) is None
            else f"{client} ({req.remote_addr})"
        )

        log_payload["extra"] = raw_payload

        return cls.parse_obj(log_payload)


def create_sftp_client() -> SFTPClient:
    """Creates a new SFTP client instance. This isn't just a constant client as the
    socket closes after some time, so we just create a new client per request

    Returns:
        SFTPClient: a new SFTP client
    """

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())

    ssh.connect(
        hostname=environ["SFTP_HOSTNAME"],
        username=environ["SFTP_USERNAME"],
        key_filename=environ["SFTP_KEY_FILEPATH"],
    )
    sftp_client = ssh.open_sftp()

    return sftp_client


@on_exception()  # type: ignore[misc]
def _create_log_string(record: LogRecord, message_only: bool = False) -> str:
    """Builds a log string from a record, to be written to a file or a console

    Args:
        record (LogRecord): the record to get parse
        message_only (bool): only return the log message, not the full string/line

    Returns:
        str: the message to write elsewhere
    """
    log_payload = loads(record.getMessage())

    client = log_payload.pop("client", "unknown")
    log_message: str = log_payload.pop("message", None)

    # If there's more data, then append it
    if len(extra := log_payload.get("extra", {})) > 0:
        extra_data_suffix = f"Extra data: {dumps(extra, default=str, sort_keys=True)}"
        log_message = (
            f"{log_message.rstrip('.')}. {extra_data_suffix}"
            if log_message
            else extra_data_suffix
        )

    if message_only:
        return log_message

    log_str = "\t".join(
        [
            datetime.fromtimestamp(record.created).strftime("%Y-%m-%d %H:%M:%S"),
            f"[{record.levelname}]",
            client,
            log_message,
        ]
    )

    return log_str


@on_exception()  # type: ignore[misc]
def log_record_to_sftp(record: LogRecord) -> None:
    """Log records to a remote file when they expire from the ListHandler

    Args:
        record (LogRecord): the expired record
    """

    sftp_client = create_sftp_client()
    sftp_client.chdir("/")
    for dir_ in SFTP_LOG_PATH.split("/"):
        try:
            sftp_client.chdir(dir_)
        except FileNotFoundError:
            sftp_client.mkdir(dir_)
            sftp_client.chdir(dir_)

    log_str = _create_log_string(record)

    with sftp_client.open(
        datetime.fromtimestamp(record.created).strftime("%Y%m%d.log"), "a"
    ) as fout:
        fout.write(log_str)
        fout.write("\n")

    sftp_client.close()


def log_record_to_local_temp(record: LogRecord) -> None:
    """Log records to a flat file when they expire from the ListHandler

    Args:
        record (LogRecord): the expired record
    """

    log_str = _create_log_string(record)

    with open(
        force_mkdir(
            user_data_dir(
                project_name="rss_log_feed",
                file_name=datetime.fromtimestamp(record.created).strftime("%Y%m%d.log"),
            ),
            path_is_file=True,
        ),
        "a",
        encoding="utf-8",
    ) as fin:
        fin.write(log_str)
        fin.write("\n")


@app.route("/feed/logs", methods=["GET"])
def get_log_feed() -> Response:
    """API endpoint for getting the current media payload dict"""

    if (level := request.args.get("level")) is None:
        record_list = LH.records
    else:
        try:
            record_list = getattr(LH, f"{level}_records")
        except AttributeError:
            return Response(f"Invalid level: {level!r}", status=400)

    feed_gen = FeedGenerator()
    feed_gen.title("Home Assistant Remote Log Feed")
    feed_gen.description("Externally-writeable log feed")
    feed_gen.link(href="http://homeassistant.local:8123", rel="self")

    for record in record_list:
        record_payload = loads(record.getMessage())

        entry = feed_gen.add_entry()
        # Use the title field for client info
        entry.title(record_payload.pop("client"))
        entry.link(
            href=record_payload.pop("link", "http://homeassistant.local:8123"),
            rel="self",
        )
        entry.published(datetime.fromtimestamp(record.created, tz=LOCAL_TZ))
        entry.category({"label": record.levelname, "term": record.levelname})
        entry.description(_create_log_string(record, message_only=True))

    response = make_response(feed_gen.rss_str())

    response.headers.set(  # type: ignore[no-untyped-call]
        "Content-Type", "application/rss+xml"
    )

    return response


@app.route("/log/<level>", methods=["POST"])
def log(level: str) -> Response:
    """API endpoint for getting the current media payload dict"""

    if (not isinstance(level, str)) or (
        level_num := NAME_TO_LEVEL.get(level.upper())
    ) is None:
        LOGGER.error("Invalid log level: %s", level)
        return Response(f"Invalid level: {str(level)!r}", status=400)

    try:
        log_payload = LogPayload.from_request(request)
    except ValidationError as exc:
        LOGGER.exception(exc)
        return Response(
            dumps(
                {
                    "error": "Invalid request body. "
                    "If payload is JSON, `message` key must be provided",
                    "traceback": format_exc(),
                    "exception": str(exc),
                }
            ),
            status="400",
        )

    RECORD_COLLECTOR.log(level_num, dumps(log_payload.dict()))

    return Response(status=200)


if __name__ == "__main__":
    # Doing this here to stop me putting all this in a gross order
    LH.on_record = log_record_to_sftp

    app.run(host="0.0.0.0", port=8001)
