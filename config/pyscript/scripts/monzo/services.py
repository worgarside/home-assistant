"""Monzo-specific services"""
from datetime import datetime
from json import dumps
from socket import gethostname
from typing import Any, Callable

from helpers import HAExceptionCatcher, get_secret
from requests import get
from requests.exceptions import ConnectionError as RequestsConnectionError
from wg_utilities.clients import MonzoClient

if gethostname() != "homeassistant":
    # pylint: disable=ungrouped-imports
    from helpers import local_setup

    log, async_mock, sync_mock, decorator, _ = local_setup()
    task = async_mock
    sensor = sync_mock
    sensor.local_ip = "0.0.0.0"
    service: Callable[..., Callable[..., Any]] = decorator

    CACHE_PATH = None
else:
    CACHE_PATH = "/config/.credentials/monzo_api_creds.json"

MODULE_NAME = "monzo"

MONZO = MonzoClient(
    client_id=get_secret("client_id", module=MODULE_NAME),
    client_secret=get_secret("client_secret", module=MODULE_NAME),
    redirect_uri=f"http://{sensor.local_ip}:5001/get_auth_code",
    creds_cache_path=CACHE_PATH,
)


@service
def top_up_credit_card_pot(top_up_amount: float) -> None:
    """Top up the Monzo credit card pot with a chosen amount

    Args:
        top_up_amount (float): the amount of money to put into the pot, in GBP

    Raises:
        Exception: if something goes wrong in the entire process. AN attempt is made
         to kill the temp server is made if this occurs
    """
    # convert GBP into pence
    top_up_amount = round(top_up_amount * 100)

    with HAExceptionCatcher(MODULE_NAME, "top_up_credit_card_pot"):
        try:
            credit_card_pot = task.executor(MONZO.get_pot_by_name, "credit cards")
            log.info("DEPOSITING %f INTO %s", top_up_amount, str(credit_card_pot))
            log.info(type(credit_card_pot))
            task.executor(
                MONZO.deposit_into_pot,
                credit_card_pot,
                amount_pence=top_up_amount,
                dedupe_id=f"hass-{top_up_amount}-"
                + datetime.today().strftime("%Y%m%d%H%M%S"),
            )
        except Exception as exc:
            if hasattr(exc, "response"):
                res_json = exc.response.json()  # type: ignore[attr-defined]
                log.info(dumps(res_json, default=str))

            log.error("KILLING SERVER")
            try:
                task.executor(get, f"http://{sensor.local_ip}:5001/kill")
                log.info("KILLED")
            except (ConnectionError, RequestsConnectionError) as connection_exc:
                log.warning(
                    "UNABLE TO KILL SERVER: %s - %s",
                    type(connection_exc).__name__,
                    str(connection_exc),
                )
            raise
