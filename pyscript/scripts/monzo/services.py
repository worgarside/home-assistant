"""Monzo-specific services"""
from __future__ import annotations

from collections.abc import Callable
from datetime import datetime
from json import dumps
from socket import gethostname
from typing import Any

from helpers import HAExceptionCatcher, instantiate_client
from wg_utilities.clients import MonzoClient

if gethostname() != "homeassistant":
    # pylint: disable=ungrouped-imports
    from helpers import local_setup

    log, async_mock, sync_mock, decorator, _ = local_setup()
    task = async_mock
    sensor = sync_mock
    sensor.ipv4_address_eth0 = "0.0.0.0"
    service: Callable[..., Callable[..., Any]] = decorator
    pyscript_executor: Callable[..., Callable[..., Any]] = decorator

MODULE_NAME = "monzo"

MONZO = instantiate_client(MonzoClient, MODULE_NAME)


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
            task.executor(
                MONZO.deposit_into_pot,
                credit_card_pot,
                amount_pence=top_up_amount,
                dedupe_id=f"hass-{top_up_amount}-"
                + datetime.today().strftime("%Y%m%d%H%M%S"),
            )
        except Exception as exc:
            if hasattr(exc, "response"):
                res_json = exc.response.json()
                log.info(dumps(res_json, default=str))

            raise
