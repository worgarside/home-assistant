"""Functions which can be triggered/timed and set the value(s) for variable(s)"""
from __future__ import annotations

from collections.abc import Callable
from logging import DEBUG, ERROR, getLogger
from socket import gethostname
from typing import Any

from helpers import HAExceptionCatcher, get_secret, instantiate_client
from requests import HTTPError
from wg_utilities.clients import TrueLayerClient
from wg_utilities.clients.truelayer import Bank, Card
from wg_utilities.loggers import add_warehouse_handler

MODULE_NAME = "truelayer"

# ToDo: Re-add HSBC client
MONZO = instantiate_client(TrueLayerClient, MODULE_NAME, bank=Bank.MONZO)
AMEX = instantiate_client(TrueLayerClient, MODULE_NAME, bank=Bank.AMEX)
SANTANDER = instantiate_client(TrueLayerClient, MODULE_NAME, bank=Bank.SANTANDER)

if gethostname() != "homeassistant":
    from helpers import local_setup  # pylint: disable=ungrouped-imports

    log, task, sync_mock, _, decorator_with_args = local_setup()
    var = sync_mock
    time_trigger: Callable[[Any], Callable[..., Any]] = decorator_with_args

LOGGER = getLogger(__name__)
LOGGER.setLevel(DEBUG)

add_warehouse_handler(
    LOGGER,
    level=ERROR,
    warehouse_port=8002,
    allow_connection_errors=True,
    pyscript_task_executor=task.executor,
)


VAR_ENTITY_MAP = {}


def _populate_var_entity_map() -> None:
    """Populate the `VAR_ENTITY_MAP` with the variables and entities to update"""

    for var_name, client_method, secret_name in (
        ("monzo_current_account", MONZO.get_account_by_id, "monzo_current_account_id"),
        ("monzo_savings", MONZO.get_account_by_id, "monzo_savings_pot_id"),
        ("monzo_credit_cards", MONZO.get_account_by_id, "monzo_credit_cards_pot_id"),
        ("amex", AMEX.get_card_by_id, "amex_card_id"),
        (
            "santander_current_account",
            SANTANDER.get_account_by_id,
            "santander_current_account_id",
        ),
        (
            "santander_savings_account",
            SANTANDER.get_account_by_id,
            "santander_savings_account_id",
        ),
    ):
        try:
            secret = get_secret(secret_name, module=MODULE_NAME)
        except Exception as exc:  # pylint: disable=broad-exception-caught
            LOGGER.exception(
                "Unable to get secret `%s` for variable `%s`: %s - %s",
                secret_name,
                var_name,
                type(exc).__name__,
                str(exc),
            )
            continue

        try:
            VAR_ENTITY_MAP[var_name] = task.executor(client_method, secret)
        except HTTPError as exc:
            LOGGER.exception(
                "Error authenticating TrueLayer client for variable `%s`: %s %s; %s",
                var_name,
                exc.response.status_code,
                exc.response.reason,
                exc.response.text,
            )
        except Exception as exc:  # pylint: disable=broad-exception-caught
            LOGGER.exception(
                "Unable to get entity for variable `%s`: %s - %s",
                var_name,
                type(exc).__name__,
                str(exc),
            )


# Mapping of the variable names to the Account/Card instances themselves
with HAExceptionCatcher(MODULE_NAME, "instantiate_truelayer_accounts"):
    _populate_var_entity_map()


@time_trigger("cron(*/5 * * * *)")
def update_balance_variables() -> None:
    """Update all TrueLayer balance variables as defined by `VAR_ENTITY_MAP`"""
    log.info("time to get values")
    with HAExceptionCatcher(MODULE_NAME, "update_balance_variables"):
        for var_name_suffix, entity in VAR_ENTITY_MAP.items():
            var_name = f"var.truelayer_balance_{var_name_suffix}"
            attr_name = (
                "current_balance" if isinstance(entity, Card) else "available_balance"
            )
            try:
                balance = task.executor(getattr, entity, attr_name)

                var.set(entity_id=var_name, value=balance, force_update=True)
            except Exception as exc:
                LOGGER.error(
                    "Unable to update variable `%s`: %s - %s",
                    var_name,
                    type(exc).__name__,
                    str(exc),
                )
                var.set(entity_id=var_name, value="unknown", force_update=True)
                raise
