"""Polls Spotify's web API for recently liked songs and adds them to monthly playlists
"""
from datetime import datetime
from json import dumps
from socket import gethostname

from wg_utilities.clients.spotify_client import SpotifyClient

from helpers import local_setup, get_secret

MODULE_NAME = "spotify.monthlies"

if gethostname() != "homeassistant":
    log, _, task, service = local_setup()
    _, _, persistent_notification, _ = local_setup()

ALL_SCOPES = [
    "ugc-image-upload",
    "user-read-recently-played",
    "user-top-read",
    "user-read-playback-position",
    "user-read-playback-state",
    "user-modify-playback-state",
    "user-read-currently-playing",
    "app-remote-control",
    "streaming",
    "playlist-modify-public",
    "playlist-modify-private",
    "playlist-read-private",
    "playlist-read-collaborative",
    "user-follow-modify",
    "user-follow-read",
    "user-library-modify",
    "user-library-read",
    "user-read-email",
    "user-read-private",
]
SPOTIFY = SpotifyClient(
    client_id=get_secret("client_id", module=MODULE_NAME),
    client_secret=get_secret("client_secret", module=MODULE_NAME),
    scope=SpotifyClient.ALL_SCOPES,
    log_requests=True,
    creds_cache_path="/config/.spotify_cache",
)


def get_monthly_playlists():
    """Gets all monthly playlists from Spotify (based on name)

    Returns:
        list: a list of Playlist instances

    Raises:
        ValueError: if a ValueError is raised for a reason other than the playlist
         name not matching the given datetime format
    """

    monthly_playlists = []
    for playlist in task.executor(getattr, SPOTIFY, "playlists"):
        try:
            datetime.strptime(playlist.name, "%B '%y")
            monthly_playlists.append(playlist)
        except ValueError as exc:
            if str(exc) not in (
                f"time data '{playlist.name}' does not match format \"%B '%y\"",
                f'time data "{playlist.name}" does not match format "%B \'%y"',
            ):
                raise

    return monthly_playlists


@service
def update_spotify_monthlies():
    """Updates all Spotify monthly playlists!"""

    log.info("Resetting all Spotify client properties")
    SPOTIFY.reset_properties()

    recently_liked = task.executor(SPOTIFY.get_recently_liked_tracks, day_limit=7)

    # Get monthlies from past year
    monthly_playlists = sorted(
        get_monthly_playlists(),
        key=lambda playlist: datetime.strptime(playlist.name, "%B '%y"),
    )[-2:]

    all_monthly_playlist_track_ids = set()
    for playlist in monthly_playlists:
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

    if playlist_updates:
        # Need this if statement because the below throws a KeyError if the dict is
        # empty..?
        log.info(
            "Updates to be made: %s",
            dumps(
                {p.name: t_list for p, t_list in playlist_updates.items()}, default=str
            ),
        )

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
