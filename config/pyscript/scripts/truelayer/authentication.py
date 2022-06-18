"""Functions/services for TrueLayer authentication"""
from socket import gethostname

from helpers import get_secret
from wg_utilities.clients import TrueLayerClient
from wg_utilities.clients.truelayer import Bank

MODULE_NAME = "truelayer"

if gethostname() != "homeassistant":
    from helpers import local_setup  # pylint: disable=ungrouped-imports

    log, async_mock, sync_mock, decorator = local_setup()
    task = async_mock
    persistent_notification = sync_mock
    service = decorator

CLIENT_ID = get_secret("client_id", module=MODULE_NAME)
CLIENT_SECRET = get_secret("client_secret", module=MODULE_NAME)
CACHE_PATH = "/config/.credentials/truelayer_api_creds.json"


@service
def get_truelayer_auth_link() -> None:
    """Gets the TrueLayer authentication link from the client and outputs it as a
    persistent notification for user consumption.

    N.B.: The bank used in instantiating the client is immaterial
    """
    tlc = TrueLayerClient(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        bank=Bank.MONZO,
        log_requests=True,
    )

    persistent_notification.create(
        title="TrueLayer Auth Link", message=tlc.authentication_link
    )


@service
def authenticate_truelayer_against_bank(bank_name: str, code: str) -> None:
    """Authenticate TrueLayer against user's bank account

    Args:
        bank_name (str): name of the bank (must be a valid entry for Bank)
        code (str): the auth code returned from the TL auth flow
    """
    bank = Bank[bank_name.upper()]

    tl_client = TrueLayerClient(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        bank=bank,
        log_requests=True,
        creds_cache_path=CACHE_PATH,
    )

    task.executor(tl_client.authenticate_against_bank, code)

    log.info("Credentials for %s added to `%s`", bank.value, tl_client.creds_cache_path)
