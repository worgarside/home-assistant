"""Functions which can be triggered/timed and set the value(s) for variable(s)"""
from __future__ import annotations

from collections.abc import Callable
from socket import gethostname
from typing import Any

from helpers import HAExceptionCatcher, get_secret, instantiate_client
from wg_utilities.clients import TrueLayerClient
from wg_utilities.clients.truelayer import Bank, Card

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


VAR_ENTITY_MAP = {}

# Mapping of the variable names to the Account/Card instances themselves
with HAExceptionCatcher(MODULE_NAME, "instantiate_monzo_accounts"):
    VAR_ENTITY_MAP.update(
        {
            "monzo_current_account": task.executor(
                MONZO.get_account_by_id,
                get_secret("monzo_current_account_id", module=MODULE_NAME),
            ),
            "monzo_savings": task.executor(
                MONZO.get_account_by_id,
                get_secret("monzo_savings_pot_id", module=MODULE_NAME),
            ),
            "monzo_credit_cards": task.executor(
                MONZO.get_account_by_id,
                get_secret("monzo_credit_cards_pot_id", module=MODULE_NAME),
            ),
        }
    )

with HAExceptionCatcher(MODULE_NAME, "instantiate_amex_account"):
    VAR_ENTITY_MAP.update(
        {
            "amex": task.executor(
                AMEX.get_card_by_id,
                get_secret("amex_card_id", module=MODULE_NAME),
            )
        }
    )

with HAExceptionCatcher(MODULE_NAME, "instantiate_santander_accounts"):
    VAR_ENTITY_MAP.update(
        {
            "santander_current_account": task.executor(
                SANTANDER.get_account_by_id,
                get_secret("santander_current_account_id", module=MODULE_NAME),
            ),
            "santander_savings_account": task.executor(
                SANTANDER.get_account_by_id,
                get_secret("santander_savings_account_id", module=MODULE_NAME),
            ),
        }
    )


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
                log.error(
                    "Unable to update variable `%s`: %s - %s",
                    var_name,
                    type(exc).__name__,
                    str(exc),
                )
                var.set(entity_id=var_name, value="unknown", force_update=True)
                raise
