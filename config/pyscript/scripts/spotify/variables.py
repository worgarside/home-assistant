"""Functions which can be triggered/timed and set the value(s) for variable(s)"""
from wg_utilities.clients.spotify_client import SpotifyClient
from socket import gethostname
from helpers import get_secret

MODULE_NAME = "spotify"

SPOTIFY = SpotifyClient(
    client_id=get_secret("client_id", module=MODULE_NAME),
    client_secret=get_secret("client_secret", module=MODULE_NAME),
    scope=SpotifyClient.ALL_SCOPES,
    creds_cache_path="/config/.spotify_cache",
)

if gethostname() != "homeassistant":
    from helpers import local_setup

    log, async_mock, sync_mock, decorator = local_setup()
    task = async_mock
    state = sync_mock
    var = sync_mock
    state_trigger = decorator


@state_trigger("sensor.spotify_matt_scott_media_title")
@state_trigger("sensor.spotify_tom_jones_media_title")
@state_trigger("sensor.spotify_will_garside_media_title")
def get_current_tempo(var_name, value):
    """Get the tempo for the currently playing song and update the relevant variable
    with the new value

    Args:
        var_name (str): the sensor which triggered this function
        value (str): the value of the sensor
    """

    user_full_name = var_name.replace("sensor.spotify_", "").replace("_media_title", "")

    if value in ("unknown", None, ""):
        var.set(
            entity_id=f"var.spotify_bpm_{user_full_name.split('_')[0]}", value="unknown"
        )
        return

    track_id = (
        state.getattr(f"media_player.spotify_{user_full_name}")
        .get("media_content_id")
        .replace("spotify:track:", "")
    )

    track = task.executor(SPOTIFY.get_track_by_id, track_id)

    tempo = task.executor(getattr, track, "tempo")

    var.set(entity_id=f"var.spotify_bpm_{user_full_name.split('_')[0]}", value=tempo)
