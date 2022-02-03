"""Functions which can be triggered/timed and set the value(s) for variable(s)"""
from socket import gethostname

from wg_utilities.clients import TrueLayerClient
from wg_utilities.clients.truelayer import Bank, Card

from helpers import get_secret

MODULE_NAME = "truelayer"
CACHE_PATH = get_secret("creds_cache_path", module=MODULE_NAME)

TLC_ARGS = dict(
    client_id=get_secret("client_id", module=MODULE_NAME),
    client_secret=get_secret("client_secret", module=MODULE_NAME),
    log_requests=False,
    creds_cache_path=CACHE_PATH,
)

MONZO = TrueLayerClient(bank=Bank.MONZO, **TLC_ARGS)

AMEX = TrueLayerClient(bank=Bank.AMEX, **TLC_ARGS)

HSBC = TrueLayerClient(bank=Bank.HSBC, **TLC_ARGS)

SANTANDER = TrueLayerClient(bank=Bank.SANTANDER, **TLC_ARGS)

if gethostname() != "homeassistant":
    from helpers import local_setup

    log, async_mock, sync_mock, decorator = local_setup()
    task = async_mock
    var = sync_mock
    time_trigger = decorator

_INSTANCE_KWARGS = {"balance_update_threshold": 1}

# Mapping of the variable names to the Account/Card instances themselves
VAR_ENTITY_MAP = {
    "monzo_current_account": task.executor(
        MONZO.get_account_by_id,
        get_secret("monzo_current_account_id", module=MODULE_NAME),
        instance_kwargs=_INSTANCE_KWARGS,
    ),
    "monzo_savings": task.executor(
        MONZO.get_account_by_id,
        get_secret("monzo_savings_pot_id", module=MODULE_NAME),
        instance_kwargs=_INSTANCE_KWARGS,
    ),
    "monzo_credit_cards": task.executor(
        MONZO.get_account_by_id,
        get_secret("monzo_credit_cards_pot_id", module=MODULE_NAME),
        instance_kwargs=_INSTANCE_KWARGS,
    ),
    "amex": task.executor(
        AMEX.get_card_by_id,
        get_secret("amex_card_id", module=MODULE_NAME),
        instance_kwargs=_INSTANCE_KWARGS,
    ),
    "hsbc_current_account": task.executor(
        HSBC.get_account_by_id,
        get_secret("hsbc_current_account_id", module=MODULE_NAME),
        instance_kwargs=_INSTANCE_KWARGS,
    ),
    "santander_current_account": task.executor(
        SANTANDER.get_account_by_id,
        get_secret("santander_current_account_id", module=MODULE_NAME),
        instance_kwargs=_INSTANCE_KWARGS,
    ),
    "santander_savings_account": task.executor(
        SANTANDER.get_account_by_id,
        get_secret("santander_savings_account_id", module=MODULE_NAME),
        instance_kwargs=_INSTANCE_KWARGS,
    ),
}


@time_trigger("cron(*/5 * * * *)")
def update_balance_variables():
    """Update all TrueLayer balance variables as defined by `VAR_ENTITY_MAP`"""

    for var_name_suffix, entity in VAR_ENTITY_MAP.items():
        var_name = f"var.truelayer_balance_{var_name_suffix}"
        attr_name = (
            "current_balance" if isinstance(entity, Card) else "available_balance"
        )
        try:
            # log.info("Getting %s from %s for %s", attr_name, str(entity), var_name)
            balance = task.executor(getattr, entity, attr_name)

            var.set(entity_id=var_name, value=balance, force_update=True)
        except Exception as exc:  # pylint: disable=broad-except
            log.error("%s - %s", type(exc).__name__, str(exc))
            var.set(entity_id=var_name, value="unknown", force_update=True)
