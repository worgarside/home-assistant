"""Services for managing SwitchBot devices via the API"""
from json import dumps
from socket import gethostname

from helpers import get_secret
from requests import post

MODULE_NAME = "switchbot.curtain_controller"

if gethostname() != "homeassistant":
    from helpers import local_setup  # pylint: disable=ungrouped-imports

    log, async_mock, sync_mock, decorator = local_setup()
    task = async_mock
    sensor = sync_mock
    input_number = sync_mock
    service = decorator


API_KEY = get_secret("api_key", module=MODULE_NAME)
CURTAIN_ID = get_secret("curtain_id", module=MODULE_NAME)
BASE_URL = "https://api.switch-bot.com"
HEADERS = {"Authorization": API_KEY, "Content-Type": "application/json; charset=utf8"}


@service
def open_curtain() -> None:
    """Opens the SwitchBot curtain"""

    log.info("Opening curtain...")
    set_curtain_position(0)


@service
def close_curtain() -> None:
    """Closes the SwitchBot curtain"""

    log.info("Closing curtain")
    set_curtain_position(100)


@service
def set_curtain_position(position: int, index: int = 0, mode: str = "ff") -> None:
    """Sets the SwitchBot curtain to a given position

    Args:
        position (int): the position to set the curtain to
        index (int): I still don't know :(
        mode (str): the mode (performance etc.) to use when moving the SwitchBot
    """
    if (
        delta := abs(
            (sensor_val := int(sensor.will_s_room_curtain_position)) - position
        )
    ) > 5:
        log.info("Setting curtain position to %i", position)
        res = task.executor(
            post,
            f"{BASE_URL}/v1.0/devices/{CURTAIN_ID}/commands",
            json={
                "command": "setPosition",
                "parameter": ",".join(map(str, [index, mode, position])),
                "commandType": "command",
            },
            headers=HEADERS,
        )

        log.debug(dumps(res.json(), default=str))
    else:
        log.info(
            "Change too small (%i), "
            "changing input_number.wills_room_curtain_position to %i",
            delta,
            sensor_val,
        )
        input_number.set_value(
            entity_id="input_number.wills_room_curtain_position", value=sensor_val
        )
