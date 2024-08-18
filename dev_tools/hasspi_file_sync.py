"""Syncs files from the home-assistant repository to the HAssPi."""

from __future__ import annotations

from datetime import datetime
from logging import getLogger
from pathlib import Path
from time import sleep, time

from paramiko import AutoAddPolicy, SFTPClient, SSHClient, SSHConfig
from watchdog.events import (
    DirCreatedEvent,
    DirDeletedEvent,
    DirModifiedEvent,
    DirMovedEvent,
    FileCreatedEvent,
    FileDeletedEvent,
    FileSystemEvent,
    FileSystemEventHandler,
)
from watchdog.observers import Observer
from wg_utilities.loggers import add_stream_handler

LOGGER = getLogger(__name__)
LOGGER.setLevel("DEBUG")
add_stream_handler(LOGGER)

REPO_PATH = Path(__file__).parents[2]


if REPO_PATH.name != "home-assistant" or not REPO_PATH.is_dir():
    raise RuntimeError(
        "Unable to locate the `home-assistant` repository."
        f" Current path is: {REPO_PATH!s}",
    )

OBSERVER = Observer()


class FileSyncHandler(FileSystemEventHandler):
    """Sync files to the HAssPi on FileSystem events."""

    _sftp_client: SFTPClient

    def __init__(self, ssh_client: SSHClient) -> None:
        """Initialize the FileSyncHandler."""
        self._ssh_client = ssh_client

        self._last_sftp_use = 0

    def _delete_file_from_hasspi(
        self,
        event: FileSystemEvent,
    ) -> None:
        """Delete a file from the HAssPi.

        Args:
            event (DirDeletedEvent | FileDeletedEvent): The event.
        """
        file_path = Path(event.src_path).relative_to(REPO_PATH)

        if self._path_is_ignored(file_path=file_path):
            LOGGER.debug("Ignoring %s deletion", file_path.as_posix())
            return

        target_path = Path("/config") / file_path

        try:
            self.sftp_client.remove(target_path.as_posix())
            LOGGER.info("Deleted %s", target_path.as_posix())
        except FileNotFoundError as exc:
            LOGGER.debug("Delete failed successfully? %r", exc)

    @staticmethod
    def _path_is_ignored(
        *,
        file_path: Path | None = None,
        src_path: str | None = None,
        must_exist: bool = False,
    ) -> bool:
        """Check if a path should be ignored.

        Args:
            file_path (Path): The file path, relative to REPO_PATH
            src_path (str): The event's source path
            must_exist (bool): If the path must exist in the repository.

        Returns:
            bool: True if the path should be ignored.

        Raises:
            ValueError: If neither `file_path` or `src_path` are provided.
        """
        if src_path:
            file_path = Path(src_path).relative_to(REPO_PATH)

        if not file_path:
            raise ValueError(
                "Must provide either `file_path` or `src_path`",
            )

        if file_path.as_posix().startswith(".") or file_path.suffix in {
            ".pyc",
            ".isorted",
        }:
            return True

        if must_exist:
            return not REPO_PATH.joinpath(file_path).exists()

        return False

    def _write_file_to_hasspi(
        self,
        event: FileSystemEvent,
    ) -> None:
        """Write a file to the HAssPi."""
        file_path = Path(event.src_path).relative_to(REPO_PATH)

        if event.is_directory or self._path_is_ignored(
            file_path=file_path,
            must_exist=True,
        ):
            LOGGER.debug("Ignoring %s write event", file_path.as_posix())
            return

        target_path = Path("/config") / file_path

        try:
            self.sftp_client.put(event.src_path, target_path.as_posix())
            LOGGER.info("%s -> %s", file_path.as_posix(), target_path.as_posix())
        except FileNotFoundError:
            for directory in target_path.parts[:-1]:
                try:
                    self.sftp_client.chdir(directory)
                except FileNotFoundError:  # noqa: PERF203
                    LOGGER.debug("Creating directory: %s", directory)
                    self.sftp_client.mkdir(directory)
                    self.sftp_client.chdir(directory)

            self.sftp_client.put(event.src_path, target_path.as_posix())
            LOGGER.info("Wrote %s -> %s", file_path.as_posix(), target_path.as_posix())

    def on_created(self, event: DirCreatedEvent | FileSystemEvent) -> None:
        """Handle a file or directory being created."""
        self._write_file_to_hasspi(event)

    def on_deleted(self, event: DirDeletedEvent | FileSystemEvent) -> None:
        """Handle a file or directory being deleted."""
        self._delete_file_from_hasspi(event)

    def on_modified(self, event: DirModifiedEvent | FileSystemEvent) -> None:
        """Handle a file or directory being modified."""
        self._write_file_to_hasspi(event)

    def on_moved(self, event: DirMovedEvent | FileSystemEvent) -> None:
        """Handle a file or directory being moved."""
        if self._path_is_ignored(src_path=event.src_path):
            LOGGER.debug("Ignoring %s move", event.src_path)
            return

        delete_event: DirDeletedEvent | FileDeletedEvent = (
            DirDeletedEvent(event.src_path)
            if event.is_directory
            else FileDeletedEvent(event.src_path)
        )
        write_event: DirCreatedEvent | FileCreatedEvent = (
            DirCreatedEvent(event.dest_path)
            if event.is_directory
            else FileCreatedEvent(event.dest_path)
        )

        self._delete_file_from_hasspi(delete_event)
        self._write_file_to_hasspi(write_event)

    @property
    def sftp_client(self) -> SFTPClient:
        """Get the SFTP client.

        If the client has not been used in the last 60 seconds, a connection check is
        done and the client is re-instantiated if it does not succeed.

        Returns:
            SFTPClient: The SFTP client.
        """
        if not hasattr(self, "_sftp_client"):
            LOGGER.debug("Creating SFTP client")
            self._sftp_client = self._ssh_client.open_sftp()

            self._last_sftp_use = int(time())
            return self._sftp_client

        if self._last_sftp_use < int(time()) - 60:
            LOGGER.debug(
                "Checking SFTP connection. Last use: %s",
                datetime.fromtimestamp(self._last_sftp_use).isoformat(),  # noqa: DTZ006
            )
            try:
                self._sftp_client.stat(".")
                LOGGER.debug("OK")
            except OSError as exc:
                LOGGER.debug("Failed: %s", exc)
                self._ssh_client = create_ssh_client()
                self._sftp_client = self._ssh_client.open_sftp()
                LOGGER.debug("Recreated SFTP client")

        self._last_sftp_use = int(time())
        return self._sftp_client


def create_ssh_client() -> SSHClient:
    """Create an SSH client for the HAssPi.

    Returns:
        SSHClient: The SSH client.
    """
    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())  # noqa: S507

    ssh_config = SSHConfig.from_path(Path("~/.ssh/config").expanduser().as_posix())

    hasspi_config = ssh_config.lookup("hasspi")

    try:
        ssh_client.connect(
            hostname=hasspi_config["hostname"],
            username=hasspi_config["user"],
            port=int(hasspi_config.get("port", "22")),
            key_filename=hasspi_config.get("identityfile", [])[0],
            timeout=10,
        )
    except (LookupError, ValueError):
        LOGGER.exception("Unable to find `hasspi` config in ~/.ssh/config")
        LOGGER.debug(repr(hasspi_config))

        raise

    return ssh_client


def main() -> None:
    """Run the file sync."""
    ssh_client = create_ssh_client()

    event_handler = FileSyncHandler(ssh_client)
    OBSERVER.schedule(  # type: ignore[no-untyped-call]
        event_handler,
        path=REPO_PATH,
        recursive=True,
    )
    OBSERVER.start()  # type: ignore[no-untyped-call]
    LOGGER.info("Watching %s", REPO_PATH)
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        OBSERVER.stop()  # type: ignore[no-untyped-call]
    ssh_client.close()
    OBSERVER.join()


if __name__ == "__main__":
    main()
