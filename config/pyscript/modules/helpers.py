"""helper functions for use across Pyscript"""

from socket import gethostname
from unittest.mock import MagicMock


# pylint: disable=import-outside-toplevel
def local_setup():
    """Helper function for creation of fake/stubbed variables which are automatically
    available to Pyscript

    Returns:
        Logger: a logger
        AsyncMock: an asynchronous mock object
        MagicMock: a synchronous mock object
        function: a function to be used as any decorator - it does nothing
    """
    from logging import getLogger, DEBUG
    from wg_utilities.loggers import add_stream_handler
    from unittest.mock import AsyncMock

    def _dummy_decorator(func):
        """Dummy function for running scripts locally"""
        return func

    _log = getLogger(__name__)
    _log.setLevel(DEBUG)
    add_stream_handler(_log)

    return _log, AsyncMock(), MagicMock(), _dummy_decorator


if gethostname() != "homeassistant":
    log, _, pyscript, _ = local_setup()


def get_secret(secret_name, *, module, default=None):
    """Get a secret from Home Assistant (similar to `os.getenv` really)

    Args:
        secret_name (str): the name of the secret to retrieve
        module (str): the name of the module which the secret is for
        default (str): the default value to return

    Returns:
        str: the secret's value
    """
    return pyscript.config.get("apps", {}).get(module, {}).get(secret_name, default)
