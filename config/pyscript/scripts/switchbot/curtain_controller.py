"""Services for managing SwitchBot devices via the API"""
from json import dumps
from socket import gethostname
from typing import Any, Callable

from helpers import get_secret
from requests import post

MODULE_NAME = "switchbot.curtain_controller"

if gethostname() != "homeassistant":
    from helpers import local_setup  # pylint: disable=ungrouped-imports

    log, task, sync_mock, decorator, _ = local_setup()
    sensor = sync_mock
    binary_sensor = sync_mock
    cover = sync_mock
    homeassistant = sync_mock
    service: Callable[..., Callable[..., Any]] = decorator


API_KEY = get_secret("api_key", module=MODULE_NAME)
CURTAIN_ID = get_secret("curtain_id", module=MODULE_NAME)
BASE_URL = "https://api.switch-bot.com"
HEADERS = {"Authorization": API_KEY, "Content-Type": "application/json; charset=utf8"}


@service
def set_curtain_position(position: int, index: int = 0, mode: str = "ff") -> None:
    """Sets the SwitchBot curtain to a given position

    Args:
        position (int): the position to set the curtain to
        index (int): I still don't know :(
        mode (str): the mode (performance etc.) to use when moving the SwitchBot
    """

    # If the balcony door is open, only close the curtain to 15%
    if binary_sensor.will_s_balcony_door == "on" and position < 15:
        log.warning("Limiting curtain position to 15% as balcony door is open")
        position = 15
        cover.set_cover_position(
            position=position, entity_id="cover.wills_room_curtain"
        )
    else:
        log.info("Setting curtain position to %i", position)
        res = task.executor(
            post,
            f"{BASE_URL}/v1.0/devices/{CURTAIN_ID}/commands",
            json={
                "command": "setPosition",
                # 100 - position here to account for SwitchBot/HA 0-100 flip
                "parameter": ",".join(map(str, [index, mode, 100 - position])),
                "commandType": "command",
            },
            headers=HEADERS,
        )

        log.info(dumps(res.json(), default=str))
