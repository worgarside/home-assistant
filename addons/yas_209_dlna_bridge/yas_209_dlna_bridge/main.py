"""Custom addon to listen to the YAS-209 and post updates to HA"""
from datetime import datetime
from io import BytesIO
from json import dumps
from logging import DEBUG, getLogger
from os import environ, getenv
from typing import Any, Dict, Optional, TypedDict

from dotenv import load_dotenv
from paramiko import AutoAddPolicy, SFTPClient, SSHClient
from requests import post

# pylint: disable=no-name-in-module
from wg_utilities.devices.yamaha_yas_209 import YamahaYas209
from wg_utilities.devices.yamaha_yas_209.yamaha_yas_209 import CurrentTrack
from wg_utilities.exceptions import on_exception
from wg_utilities.loggers import add_stream_handler

load_dotenv()

LOGGER = getLogger(__name__)
LOGGER.setLevel(DEBUG)
add_stream_handler(LOGGER)


class PayloadInfo(TypedDict):
    """Info for the PAYLOAD constant"""

    state: Optional[str]
    album_art_uri: Optional[str]
    volume_level: Optional[float]
    media_duration: Optional[float]
    media_title: Optional[str]
    media_artist: Optional[str]
    media_album_name: Optional[str]


TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S.%f"


@on_exception()  # type: ignore[misc]
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
def log_request_payload(event_payload: Dict[str, Any]) -> None:
    """Log the request payload locally for archiving etc.

    Args:
        event_payload (dict): the payload received from the YAS-209
    """

    if (last_change := event_payload.get("last_change")) is not None:
        event_payload["last_change"] = last_change.dict()

    event_timestamp = event_payload.get("timestamp", datetime.now())

    file_path = event_timestamp.strftime("config/.addons/yas_209_dlna_bridge/%Y/%m/%d")
    file_name = event_timestamp.strftime("payload_%Y%m%d%H%M%S%f.json")

    sftp_client = create_sftp_client()

    sftp_client.chdir("/")
    for dir_ in file_path.split("/"):
        try:
            sftp_client.chdir(dir_)
        except FileNotFoundError:
            sftp_client.mkdir(dir_)
            sftp_client.chdir(dir_)

    sftp_client.putfo(
        BytesIO(dumps(event_payload, indent=2, default=str).encode()), file_name
    )

    LOGGER.debug(
        "Logged %s payload to '%s/%s'",
        event_payload.get("service_id", "unknown").split(":")[-1],
        file_path,
        file_name,
    )

    sftp_client.close()


@on_exception()  # type: ignore[misc]
def pass_data_to_home_assistant() -> None:
    """Sends the payload to HA. The payload is global as we don't want to remove track
    metadata on a volume update, for example. The data should persist unless explicitly
     removed
    """

    res = post(
        "http://homeassistant.local:8123/api/webhook/wills_yas_209_bridge_input",
        json=PAYLOAD,
        headers={"Content-Type": "application/json"},
        timeout=10,
    )

    LOGGER.debug("Webhook response: %i %s", res.status_code, res.reason)

    res.raise_for_status()


def on_volume_update(volume: float) -> None:
    """Callback for volume updates

    Args:
        volume (float): the new volume level
    """

    LOGGER.debug("Volume updated to %f", volume)

    PAYLOAD["volume_level"] = volume

    pass_data_to_home_assistant()


@on_exception()  # type: ignore[misc]
def on_state_update(state: str) -> None:
    """Callback for state updates

    Args:
        state (str): the new state
    """
    LOGGER.debug("State updated to %s", state)

    PAYLOAD["state"] = state

    pass_data_to_home_assistant()


@on_exception()  # type: ignore[misc]
def on_track_update(track: CurrentTrack.Info) -> None:
    """Callback for track updates

    Args:
        track (CurrentTrack.Info): the track metadata
    """
    LOGGER.debug("Track updated to %s", dumps(track, default=str))

    PAYLOAD.update(track)

    pass_data_to_home_assistant()


PAYLOAD: PayloadInfo = {
    "state": None,
    "album_art_uri": None,
    "volume_level": None,
    "media_duration": None,
    "media_title": None,
    "media_artist": None,
    "media_album_name": None,
}


YAS_209 = YamahaYas209(
    "10.0.0.21",
    on_event=log_request_payload,
    on_volume_update=on_volume_update,
    on_state_update=on_state_update,
    on_track_update=on_track_update,
    start_listener=True,
    listen_ip=None
    if (listen_ip := getenv("LISTEN_IP", "null").lower()) == "null"
    else listen_ip,
    listen_port=None
    if (listen_port := getenv("LISTEN_PORT", "null").lower()) == "null"
    else int(listen_port),
    source_port=None
    if (source_port := getenv("SOURCE_PORT", "null").lower()) == "null"
    else int(source_port),
)


PAYLOAD["state"] = YAS_209.state.value
PAYLOAD["volume_level"] = YAS_209.volume_level
