"""Functions/services for TrueLayer authentication"""
from __future__ import annotations

from collections.abc import Callable
from socket import gethostname
from typing import Any

from helpers import HAExceptionCatcher, instantiate_client
from wg_utilities.clients import TrueLayerClient
from wg_utilities.clients.truelayer import Bank

MODULE_NAME = "truelayer"

if gethostname() != "homeassistant":
    from helpers import local_setup  # pylint: disable=ungrouped-imports

    log, task, _, decorator, __ = local_setup()
    service: Callable[..., Callable[..., Any]] = decorator


@service
def authenticate_truelayer_against_bank(bank_name: str) -> None:
    """Authenticate TrueLayer against user's bank account

    Args:
        bank_name (str): name of the bank (must be a valid entry for Bank)
    """
    bank = Bank[bank_name.upper()]

    with HAExceptionCatcher(MODULE_NAME, "authenticate_truelayer_against_bank"):
        tl_client = instantiate_client(TrueLayerClient, MODULE_NAME, bank=bank)

        task.executor(tl_client.refresh_access_token)

        log.info(
            "Credentials for %s added to `%s`", bank.value, tl_client.creds_cache_path
        )
