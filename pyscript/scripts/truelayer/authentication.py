"""Functions/services for TrueLayer authentication"""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from socket import gethostname
from typing import Any

from helpers import HAExceptionCatcher, get_secret
from wg_utilities.clients import TrueLayerClient
from wg_utilities.clients.truelayer import Bank

MODULE_NAME = "truelayer"

if gethostname() != "homeassistant":
    from helpers import local_setup  # pylint: disable=ungrouped-imports

    log, task, sync_mock, decorator, _ = local_setup()
    persistent_notification = sync_mock
    service: Callable[..., Callable[..., Any]] = decorator

CLIENT_ID = get_secret("client_id", module=MODULE_NAME)
CLIENT_SECRET = get_secret("client_secret", module=MODULE_NAME)
CACHE_PATH = Path("/config/.credentials/truelayer_api_creds.json")


@service
def authenticate_truelayer_against_bank(bank_name: str) -> None:
    """Authenticate TrueLayer against user's bank account

    Args:
        bank_name (str): name of the bank (must be a valid entry for Bank)
    """
    bank = Bank[bank_name.upper()]

    with HAExceptionCatcher(MODULE_NAME, "authenticate_truelayer_against_bank"):
        tl_client = TrueLayerClient(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            bank=bank,
            log_requests=True,
            creds_cache_path=CACHE_PATH,
        )

        task.executor(tl_client.refresh_access_token)

        log.info(
            "Credentials for %s added to `%s`", bank.value, tl_client.creds_cache_path
        )
