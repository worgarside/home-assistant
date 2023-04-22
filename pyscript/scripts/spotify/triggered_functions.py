"""Functions which are only run on a certain trigger"""
from __future__ import annotations

from collections.abc import Callable, Iterable
from copy import deepcopy
from datetime import datetime
from os.path import isfile
from pathlib import Path
from re import compile as compile_regex
from socket import gethostname
from typing import Any, Dict, List  # noqa: UP035,F401

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


@pyscript_executor
def get_monthly_playlists(return_count: int = 12) -> list[Playlist]:
    """Gets all monthly playlists from Spotify (based on name)

    Args:
        return_count (int): the number of playlists to return (ordered by datetime,
         descending)

    Returns:
        List[Playlist]: a list of Playlist instances
    """

    if hasattr(SPOTIFY.current_user, "_playlists"):
        delattr(SPOTIFY.current_user, "_playlists")

    return sorted(
        (p for p in SPOTIFY.current_user.playlists if MONTHLY_PATTERN.match(p.name)),
        key=lambda playlist: datetime.strptime(playlist.name, "%B '%y"),
    )[-return_count:]


@service
@time_trigger("cron(*/15 * * * *)")
def process_liked_songs() -> None:
    """Calls other functions which process liked songs, to save polling Spotify's API
    twice"""

    with HAExceptionCatcher(MODULE_NAME, "process_liked_songs"):
        recently_liked = task.executor(
            SPOTIFY.current_user.get_recently_liked_tracks, day_limit=7
        )

        log.info("Found %s recently liked tracks", len(recently_liked))

        # Monthly updates

        all_monthly_playlist_tracks = set()

        for playlist in (last_3_monthly_playlists := get_monthly_playlists(3)):
            if hasattr(playlist, "_tracks"):
                delattr(playlist, "_tracks")

            all_monthly_playlist_tracks.update(
                task.executor(getattr, playlist, "tracks")
            )

        log.info(
            "Found %s tracks in playlists %s",
            len(all_monthly_playlist_tracks),
            ", ".join([p.name for p in last_3_monthly_playlists]),
        )

        monthly_updates = update_dynamic_playlists(
            deepcopy(recently_liked),
            all_monthly_playlist_tracks,
            lambda t: str(t.metadata["saved_at"].strftime("%B '%y")),
        )

        if monthly_updates:
            log.info(
                "%i monthly playlists updated: %s",
                len(monthly_updates),
                ", ".join(p.name for p in monthly_updates),
            )
        else:
            log.info("No monthly playlists updated")

        # Decade playlists

        decade_updates = update_dynamic_playlists(
            deepcopy(recently_liked),
            None,
            lambda t: str(t.release_date.year)[:3] + "0s",
        )

        if monthly_updates:
            log.info(
                "%i decade playlists updated: %s",
                len(decade_updates),
                ", ".join(p.name for p in decade_updates),
            )
        else:
            log.info("No decade playlists updated")

        # Notifications

        if monthly_updates:
            log.info("Building notification content")
            message = ""

            for playlist, tracks in monthly_updates.items():
                message += f"\n### {playlist.name}\n"
                for track in tracks:
                    message += f"- {track.name}\n"

                    log.info("Sending notification for %s", track.name)

                    notify.mobile_app_will_s_pixel_6_pro(
                        message=f'"{track.name}" added to {playlist.name}',
                        data={
                            "actions": [
                                {
                                    "action": "ADD_SONG_TO_CHILL_ELECTRONICA",
                                    "title": "Chill Electronica",
                                },
                                {
                                    "action": "ADD_SONG_TO_JAMBOX_JAMS",
                                    "title": "JAMBOX Jams",
                                },
                                {"action": "ADD_SONG_TO_BOTH", "title": "Both"},
                            ]
                        },
                    )

                    log.info("Notification sent")

            persistent_notification.create(
                title="Spotify Playlists Updated", message=message
            )


def update_dynamic_playlists(
    recently_liked: list[Track],
    already_processed_tracks: Iterable[Track] | None,
    target_name_func: Callable[[Track], str],
) -> dict[Playlist, list[Track]]:
    """Updates any dynamic playlists from a set of tracks and a naming match criteria

    Args:
        recently_liked (List[Track]): a list of recently liked tracks
        already_processed_tracks (Iterable[Track]): tracks which have already been
         processed
        target_name_func (Callable[[Track], str]): a function to derive a target
         playlist from the track's attributes

    Returns:
        dict[Playlist, List[Track]]: a dictionary of all playlists that have been
         updated
    """

    playlist_updates = {}  # type: Dict[Playlist, List[Track]]
    for track in recently_liked:
        if already_processed_tracks is None or track not in already_processed_tracks:
            log.info("Processing %s", str(track))

            target_playlist_name = target_name_func(track)

            log.info("Target playlist: %s", target_playlist_name)

            for playlist in playlist_updates:
                if playlist.name == target_playlist_name:
                    target_playlist = playlist
                    log.info("Found existing playlist %s", target_playlist_name)
                    break
            else:
                target_playlist = task.executor(
                    SPOTIFY.current_user.get_playlists_by_name, target_playlist_name
                )

                if target_playlist is None:
                    target_playlist = task.executor(
                        SPOTIFY.create_playlist,
                        name=target_playlist_name,
                        public=False,
                        collaborative=False,
                    )

            playlist_updates.setdefault(target_playlist, []).append(track)

        log.info("Processed %s", str(track))

    for playlist, tracks in playlist_updates.items():
        log.info("Adding %s to %s", ", ".join(map(str, tracks)), playlist.name)
        task.executor(SPOTIFY.add_tracks_to_playlist, tracks, playlist)

    return playlist_updates


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
            True,
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
