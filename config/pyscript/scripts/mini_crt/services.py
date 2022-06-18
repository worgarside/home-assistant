"""Services for the Mini CRT"""
from json import dumps
from socket import gethostname
from typing import Literal

from helpers import get_secret
from requests import get, put

MODULE = "nanoleaf.the_snail"

if gethostname() != "homeassistant":
    # pylint: disable=ungrouped-imports
    from helpers import local_setup

    log, task, sync_mock, decorator = local_setup()
    persistent_notification = sync_mock
    sensor = sync_mock
    homeassistant = sync_mock
    sensor.local_ip = "0.0.0.0"
    service = decorator
    pyscript_executor = decorator

SNAIL_IP = get_secret("ip_address", module=MODULE)
SNAIL_AUTH_TOKEN = get_secret("auth_token", module=MODULE)
SNAIL_URL = f"http://{SNAIL_IP}:16021/api/v1/{SNAIL_AUTH_TOKEN}"


def _save_nanoleaf_state(effect_type: Literal["current", "previous"]) -> None:
    """Save the current/previous Nanoleaf animation

    Args:
        effect_type (str): "current" or "previous"

    Raises:
        Exception: if an exception is raised, it is caught, logged, and re-raised
    """
    effect = task.executor(
        get, f"http://192.168.1.170:5000/effect/{effect_type}"
    ).json()
    media_payload = task.executor(
        get, f"http://192.168.1.170:5000/media-payload/{effect_type}"
    ).json()

    new_anim_name = (
        f"Custom: {media_payload.get('media_artist')} - "
        f"{media_payload.get('album_name')}"
    )

    log.info("Creating %s", new_anim_name)
    try:
        task.executor(
            put,
            f"{SNAIL_URL}/effects",
            headers={"Content-Type": "application/json"},
            data=dumps(
                {
                    "write": {
                        **effect,
                        "command": "add",
                        "animName": new_anim_name,
                    }
                }
            ),
        )

        persistent_notification.create(
            title="New Nanoleaf Animation saved", message=new_anim_name
        )
        homeassistant.update_entity(entity_id="light.the_snail")
    except Exception as exc:
        log.error("%s - %s", type(exc).__name__, str(exc))
        persistent_notification.create(
            title="Saving new Nanoleaf Animation failed",
            message=f"{type(exc).__name__} {str(exc)}\n{new_anim_name}",
        )
        raise


@service
def save_current_nanoleaf_state() -> None:
    """Save the current Nanoleaf state"""
    _save_nanoleaf_state("current")


@service
def save_previous_nanoleaf_state() -> None:
    """Save the previous Nanoleaf state"""
    _save_nanoleaf_state("previous")
