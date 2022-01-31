"""Functions which are only run on a certain trigger"""
from datetime import datetime
from os.path import isfile
from socket import gethostname
from re import compile as compile_regex
from requests import get
from wg_utilities.clients.spotify_client import SpotifyClient
from wg_utilities.functions import force_mkdir

from helpers import get_secret
from helpers import write_file

MODULE_NAME = "spotify"

if gethostname() != "homeassistant":
    from helpers import local_setup

    log, async_mock, sync_mock, decorator = local_setup()
    task = async_mock
    state = sync_mock
    sensor = sync_mock
    persistent_notification = sync_mock
    state_trigger = decorator
    pyscript_executor = decorator
    time_trigger = decorator

SPOTIFY = SpotifyClient(
    client_id=get_secret("client_id", module=MODULE_NAME),
    client_secret=get_secret("client_secret", module=MODULE_NAME),
    scope=SpotifyClient.ALL_SCOPES,
    creds_cache_path="/config/.spotify_cache",
)

_MONTH_LIST = "|".join(
    datetime.strptime(str(i), "%m").strftime("%B") for i in range(1, 13)
)
MONTHLY_PATTERN = compile_regex(rf"^({_MONTH_LIST}) '[0-9]{{2}}$")


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


@time_trigger("cron(*/15 * * * *)")
def update_spotify_monthlies():
    """Updates all Spotify monthly playlists!"""

    log.info("Resetting all Spotify client properties")
    SPOTIFY.reset_properties()

    recently_liked = task.executor(SPOTIFY.get_recently_liked_tracks, day_limit=7)

    all_monthly_playlist_track_ids = set()
    for playlist in get_monthly_playlists(6):
        all_monthly_playlist_track_ids.update(
            [t.id for t in task.executor(getattr, playlist, "tracks")]
        )

    playlist_updates = {}

    for track in recently_liked:
        if track.id not in all_monthly_playlist_track_ids:
            log.debug("Processing %s", str(track))

            target_playlist_name = datetime.strptime(
                track.metadata.get("liked_at"), SPOTIFY.DATETIME_FORMAT
            ).strftime("%B '%y")

            for playlist in playlist_updates:
                if playlist.name == target_playlist_name:
                    target_monthly_playlist = playlist
                    break
            else:
                target_monthly_playlist = task.executor(
                    SPOTIFY.get_playlists_by_name, target_playlist_name
                )

                if target_monthly_playlist is None:
                    target_monthly_playlist = task.executor(
                        SPOTIFY.create_playlist,
                        name=target_playlist_name,
                        public=False,
                        collaborative=False,
                    )

            if target_monthly_playlist not in playlist_updates:
                playlist_updates[target_monthly_playlist] = []

            playlist_updates[target_monthly_playlist].append(track)

    for playlist, tracks in playlist_updates.items():
        log.debug("Adding %s to %s", ", ".join(map(str, tracks)), playlist.name)
        task.executor(SPOTIFY.add_tracks_to_playlist, tracks, playlist)

    if playlist_updates:
        message = ""

        for playlist, tracks in playlist_updates.items():
            message += f"### {playlist.name}\n"
            for track in tracks:
                message += f"""- {track.name}\n"""

        persistent_notification.create(
            title="Spotify Monthlies Updated", message=message
        )

    log.info("Process complete, %i API calls made in total", SPOTIFY.api_call_count)


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
