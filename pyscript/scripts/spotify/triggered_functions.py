"""Functions which are only run on a certain trigger"""
from __future__ import annotations

from collections.abc import Callable
from datetime import datetime
from os.path import isfile
from pathlib import Path
from re import compile as compile_regex
from socket import gethostname
from typing import Any

from helpers import HAExceptionCatcher, instantiate_client, write_file
from requests import get
from wg_utilities.clients import SpotifyClient
from wg_utilities.clients.spotify import Playlist, Track
from wg_utilities.functions import force_mkdir

MODULE_NAME = "spotify"

if gethostname() != "homeassistant":
    from helpers import local_setup  # pylint: disable=ungrouped-imports

    log, task, sync_mock, decorator, decorator_with_args = local_setup()
    state = sync_mock
    sensor = sync_mock
    persistent_notification = sync_mock
    notify = sync_mock
    state_trigger: Callable[[Any], Callable[..., Any]] = decorator_with_args
    pyscript_executor: Callable[..., Callable[..., Any]] = decorator
    time_trigger: Callable[[Any], Callable[..., Any]] = decorator_with_args
    event_trigger: Callable[[Any], Callable[..., Any]] = decorator_with_args
    service: Callable[..., Callable[..., Any]] = decorator

SPOTIFY = instantiate_client(SpotifyClient, MODULE_NAME)

# Instantiate the user now so that we can use it freely later
task.executor(getattr, SPOTIFY, "current_user")

DECADE_PATTERN = compile_regex(r"^\d{3}0s$")
_MONTH_LIST = "|".join(
    [datetime.strptime(str(i), "%m").strftime("%B") for i in range(1, 13)]
)
MONTHLY_PATTERN = compile_regex(rf"^({_MONTH_LIST}) '[0-9]{{2}}$")

# Playlists
CHILL_ELECTRONICA = task.executor(SPOTIFY.get_playlist_by_id, "2lMx8FU0SeQ7eA5kcMlNpX")
JAMBOX_JAMS = task.executor(SPOTIFY.get_playlist_by_id, "4Vv023MaZsc8NTWZ4WJvIL")
PIXEL_NOW_PLAYING = task.executor(SPOTIFY.get_playlist_by_id, "7vK46qf4I352doLdlSG9G0")

_SAVE_ALBUM_ARTWORK_TRIGGER = "sensor.spotify_{}_media_album_artwork_internal_url"


@state_trigger(_SAVE_ALBUM_ARTWORK_TRIGGER.format("will_garside"))
def save_album_artwork(var_name: str, value: str, old_value: str) -> None:
    """Saves the artwork for a given album to the local file storage for use elsewhere

    Args:
        var_name (str): the sensor which triggered this function
        value (str): the value of the sensor
        old_value (str): the previous value of the sensor
    """

    if value in ("unknown", old_value):
        return

    log.info("Triggered by `%s`", var_name)

    cleansed_album_name = ""
    for char in str(state.get(var_name.replace("_artwork_internal_url", "_name"))):
        if char.isalnum():
            cleansed_album_name += char.lower()

    cleansed_artist_name = ""
    for char in str(
        state.get(var_name.replace("_album_artwork_internal_url", "_artist"))
    ):
        if char.isalnum():
            cleansed_artist_name += char.lower()

    if isfile(
        target_path := Path("/config/www/album_artwork").joinpath(
            cleansed_artist_name,
            f"{cleansed_album_name}.jpg",
        )
    ):
        return

    res = task.executor(get, f"http://{sensor.ipv4_address_eth0}:8123{value}")

    res.raise_for_status()

    log.info(
        "Album artwork endpoint response was `%s %s` - writing content to %s",
        res.status_code,
        res.reason,
        target_path,
    )

    write_file(
        force_mkdir(
            target_path,
            path_is_file=True,
        ),
        res.content,
        encoding=None,
    )


@pyscript_executor
def add_to_playlist(track: Track, playlist: Playlist) -> None:
    """Add a track to a playlist, but from PyScript...

    Args:
        track (Track): the track to add
        playlist (Playlist): the playlist to update
    """

    if track not in playlist:
        SPOTIFY.add_tracks_to_playlist(
            tracks=[track],
            playlist=playlist,
        )
        playlist.tracks.append(track)


@event_trigger("mobile_app_notification_action")
def add_track_to_playlist(action: str, message: str, **_: dict[Any, Any]) -> None:
    """Add a given track to a playlist, triggered from mobile notification

    Args:
        action (str): the action from the mobile notification
        message (str): the message displayed within the notification
        **_: any other kwargs

    Raises:
        Exception: if the desired track can't be found in the recently liked
    """

    # Other mobile notifications actions could trigger this function
    if not action.startswith("ADD_SONG_TO_"):
        return

    target_track_name = message.split(" added to ")[0].strip('"')

    log.debug("Looking for '%s'", target_track_name)

    track = None
    for track in task.executor(
        SPOTIFY.current_user.get_recently_liked_tracks, day_limit=7
    ):
        if track.name == target_track_name:
            break

    if not track:
        raise Exception(  # pylint: disable=broad-exception-raised
            f'Unable to find track "{target_track_name}" in recently liked!'
        )

    if action == "ADD_SONG_TO_BOTH":
        add_to_playlist(track, CHILL_ELECTRONICA)
        add_to_playlist(track, JAMBOX_JAMS)
    elif action == "ADD_SONG_TO_CHILL_ELECTRONICA" and track not in CHILL_ELECTRONICA:
        add_to_playlist(track, CHILL_ELECTRONICA)
    elif action == "ADD_SONG_TO_JAMBOX_JAMS" and track not in JAMBOX_JAMS:
        add_to_playlist(track, JAMBOX_JAMS)


@state_trigger("var.tasker_pixel_now_playing")
def process_now_playing(value: str) -> None:
    """Saves the artwork for a given album to the local file storage for use elsewhere

    Args:
        value (str): the value of the sensor
    """
    with HAExceptionCatcher(MODULE_NAME, "process_now_playing.search"):
        matched_track = task.executor(
            SPOTIFY.search,
            (search_term := value.replace(" by ", " ")),
            entity_types=["track"],
            get_best_match_only=True,
        )

    with HAExceptionCatcher(MODULE_NAME, "process_now_playing.add_to_playlist"):
        if matched_track is not None:
            log.info(
                "Track found for search term '%s' with ID %s",
                search_term,
                matched_track.id,
            )

            # Get current User, then current Track
            current_track = task.executor(
                getattr,
                task.executor(getattr, SPOTIFY, "current_user"),
                "current_track",
            )

            if current_track is not None and (
                current_track == matched_track
                or (
                    current_track.name == matched_track.name
                    and current_track.artists == matched_track.artists
                )
            ):
                log.info(
                    "Not adding track to playlist, it's currently playing (%s)",
                    repr(current_track),
                )
            else:
                log.info("Adding track to playlist (%s)", repr(matched_track))
                add_to_playlist(matched_track, PIXEL_NOW_PLAYING)
        else:
            log.info("No matching track found")
