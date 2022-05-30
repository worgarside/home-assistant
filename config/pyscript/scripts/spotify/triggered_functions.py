"""Functions which are only run on a certain trigger"""
from copy import deepcopy
from datetime import datetime
from os.path import isfile
from socket import gethostname
from re import compile as compile_regex

from requests import get
from wg_utilities.clients import SpotifyClient
from wg_utilities.functions import force_mkdir

from helpers import get_secret, write_file


MODULE_NAME = "spotify"

if gethostname() == "homeassistant":
    CREDS_CACHE_PATH = "/config/.spotify_cache"
else:
    from helpers import local_setup

    log, task, sync_mock, decorator = local_setup()
    state = sync_mock
    sensor = sync_mock
    persistent_notification = sync_mock
    notify = sync_mock
    state_trigger = sync_mock
    pyscript_executor = decorator
    time_trigger = sync_mock
    event_trigger = sync_mock
    service = decorator

    CREDS_CACHE_PATH = None

SPOTIFY = SpotifyClient(
    client_id=get_secret("client_id", module=MODULE_NAME),
    client_secret=get_secret("client_secret", module=MODULE_NAME),
    scope=SpotifyClient.ALL_SCOPES,
    creds_cache_path=CREDS_CACHE_PATH,
)

DECADE_PATTERN = compile_regex(r"^'\d0s$")
_MONTH_LIST = "|".join(
    [datetime.strptime(str(i), "%m").strftime("%B") for i in range(1, 13)]
)
MONTHLY_PATTERN = compile_regex(rf"^({_MONTH_LIST}) '[0-9]{{2}}$")

# Playlists
CHILL_ELECTRONICA = task.executor(SPOTIFY.get_playlist_by_id, "2lMx8FU0SeQ7eA5kcMlNpX")
JAMBOX_JAMS = task.executor(SPOTIFY.get_playlist_by_id, "4Vv023MaZsc8NTWZ4WJvIL")


@pyscript_executor
def get_monthly_playlists(return_count=12):
    """Gets all monthly playlists from Spotify (based on name)

    Args:
        return_count (int): the number of playlists to return (ordered by datetime,
         descending)

    Returns:
        list: a list of Playlist instances
    """

    return sorted(
        [p for p in SPOTIFY.playlists if MONTHLY_PATTERN.match(p.name)],
        key=lambda playlist: datetime.strptime(playlist.name, "%B '%y"),
    )[-return_count:]


@service
@time_trigger("cron(*/15 * * * *)")
def process_liked_songs():
    """Calls other functions which process liked songs, to save polling Spotify's API
    twice"""

    log.info("Resetting all Spotify client properties")
    SPOTIFY.reset_properties()

    recently_liked = task.executor(SPOTIFY.get_recently_liked_tracks, day_limit=7)

    # Monthly updates

    all_monthly_playlist_tracks = set()
    for playlist in get_monthly_playlists(6):
        all_monthly_playlist_tracks.update(task.executor(getattr, playlist, "tracks"))

    monthly_updates = update_dynamic_playlists(
        deepcopy(recently_liked),
        all_monthly_playlist_tracks,
        lambda t: datetime.strptime(
            t.metadata.get("liked_at"), SPOTIFY.DATETIME_FORMAT
        ).strftime("%B '%y"),
    )

    # Decade playlists

    all_decade_playlist_tracks = set()
    for playlist in task.executor(getattr, SPOTIFY, "playlists"):
        if DECADE_PATTERN.match(playlist.name):
            all_decade_playlist_tracks.update(
                task.executor(getattr, playlist, "tracks")
            )

    decade_updates = update_dynamic_playlists(
        deepcopy(recently_liked),
        all_decade_playlist_tracks,
        lambda t: "'" + str(t.release_date.year)[2] + "0s",
    )

    # Notifications

    if all_playlist_updates := {**monthly_updates, **decade_updates}:
        message = ""

        for playlist, tracks in all_playlist_updates.items():
            message += f"\n### {playlist.name}\n"
            for track in tracks:
                message += f"- {track.name}\n"

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

        persistent_notification.create(
            title="Spotify Playlists Updated", message=message
        )

    log.info("Process complete, %i API calls made in total", SPOTIFY.api_call_count)


def update_dynamic_playlists(
    recently_liked, already_processed_tracks, target_name_func
):
    """Updates any dynamic playlists from a set of tracks and a naming match criteria

    Args:
        recently_liked (List[Track]): a list of recently liked tracks
        already_processed_tracks (List[Track]): tracks which have already been
         processed
        target_name_func (Callable): a function to derive a target playlist from the
         track's attributes

    Returns:
        dict: a dictionary of all playlists that have been updated
    """

    playlist_updates = {}

    for track in recently_liked:
        if track not in already_processed_tracks:
            log.debug("Processing %s", str(track))

            target_playlist_name = target_name_func(track)

            for playlist in playlist_updates:
                if playlist.name == target_playlist_name:
                    target_playlist = playlist
                    break
            else:
                target_playlist = task.executor(
                    SPOTIFY.get_playlists_by_name, target_playlist_name
                )

                if target_playlist is None:
                    target_playlist = task.executor(
                        SPOTIFY.create_playlist,
                        name=target_playlist_name,
                        public=False,
                        collaborative=False,
                    )

            playlist_updates.setdefault(target_playlist, []).append(track)

    for playlist, tracks in playlist_updates.items():
        log.debug("Adding %s to %s", ", ".join(map(str, tracks)), playlist.name)
        task.executor(SPOTIFY.add_tracks_to_playlist, tracks, playlist)

    return playlist_updates


@state_trigger("sensor.spotify_matt_scott_media_album_artwork_internal_url")
@state_trigger("sensor.spotify_tom_jones_media_album_artwork_internal_url")
@state_trigger("sensor.spotify_will_garside_media_album_artwork_internal_url")
def save_album_artwork(var_name, value, old_value):
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
        target_path := "/".join(
            [
                "www",
                "album_artwork",
                cleansed_artist_name,
                f"{cleansed_album_name}.jpg",
            ]
        )
    ):
        return

    res = task.executor(get, f"http://{sensor.local_ip}:8123{value}")

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
def add_to_playlist(track, playlist):
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


@event_trigger("mobile_app_notification_action")
def add_track_to_playlist(action, message, **_):
    """Add a given track to a playlist

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
    for track in task.executor(SPOTIFY.get_recently_liked_tracks, day_limit=7):
        if track.name == target_track_name:
            break

    if not track:
        raise Exception(
            f'Unable to find track "{target_track_name}" in recently liked!'
        )

    if action == "ADD_SONG_TO_BOTH":
        add_to_playlist(track, CHILL_ELECTRONICA)
        add_to_playlist(track, JAMBOX_JAMS)
    elif action == "ADD_SONG_TO_CHILL_ELECTRONICA" and track not in CHILL_ELECTRONICA:
        add_to_playlist(track, CHILL_ELECTRONICA)
    elif action == "ADD_SONG_TO_JAMBOX_JAMS" and track not in JAMBOX_JAMS:
        add_to_playlist(track, JAMBOX_JAMS)
