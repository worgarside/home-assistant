"""Functions which can be triggered/timed and set the value(s) for variable(s)"""
from socket import gethostname
from typing import Any, Callable, Optional

from helpers import get_secret
from wg_utilities.clients import SpotifyClient

MODULE_NAME = "spotify"

SPOTIFY = SpotifyClient(
    client_id=get_secret("client_id", module=MODULE_NAME),
    client_secret=get_secret("client_secret", module=MODULE_NAME),
    scope=SpotifyClient.ALL_SCOPES,
    creds_cache_path="/config/.spotify_cache",
)

if gethostname() != "homeassistant":
    from helpers import local_setup  # pylint: disable=ungrouped-imports

    log, task, sync_mock, decorator, decorator_with_args = local_setup()
    state = sync_mock
    var = sync_mock
    state_trigger: Callable[[Any], Callable[..., Any]] = decorator_with_args
    time_trigger: Callable[[Any], Callable[..., Any]] = decorator_with_args


@time_trigger("cron(* * * * *)")
@state_trigger("sensor.spotify_matt_scott_media_title")
@state_trigger("sensor.spotify_tom_jones_media_title")
@state_trigger("sensor.spotify_will_garside_media_title")
def update_tempo_variables(var_name: Optional[str] = None) -> None:
    """Update the tempo variables every minute"""

    users_to_update = (
        (var_name.replace("sensor.spotify_", "").replace("_media_title", ""),)
        if var_name
        else (
            "matt_scott",
            "tom_jones",
            "will_garside",
        )
    )

    for user_full_name in users_to_update:
        user_first_name, _ = user_full_name.split("_")
        media_title_sensor_name = f"sensor.spotify_{user_full_name}_media_title"
        tempo_variable_name = f"var.spotify_tempo_{user_first_name}"

        media_title_state = state.get(media_title_sensor_name)

        # if media title is newer than tempo
        if state.get(f"{media_title_sensor_name}.last_changed") > state.get(
            f"{tempo_variable_name}.last_changed"
        ):
            if media_title_state in (
                "unknown",
                None,
                "",
            ):
                log.info(
                    "`%s` has state `%s`, setting `%s` to `unknown`",
                    media_title_sensor_name,
                    media_title_state,
                    tempo_variable_name,
                )
                var.set(
                    entity_id=tempo_variable_name, value="unknown", force_update=True
                )
            else:
                track_id = (
                    state.getattr(f"media_player.spotify_{user_full_name}")
                    .get("media_content_id")
                    .replace("spotify:track:", "")
                )

                track = task.executor(SPOTIFY.get_track_by_id, track_id)

                tempo = round(task.executor(getattr, track, "tempo"))

                log.info(
                    "`%s` has state `%s`, setting `%s` to `%i`",
                    media_title_sensor_name,
                    media_title_state,
                    tempo_variable_name,
                    tempo,
                )

                var.set(entity_id=tempo_variable_name, value=tempo, force_update=True)
        else:
            if media_title_state not in (
                "unknown",
                None,
                "",
            ):
                log.info("No update detected, force refreshing")
                # Just force an update of status to the same value
                var.set(
                    entity_id=tempo_variable_name,
                    value=state.get(tempo_variable_name),
                    force_update=True,
                )
