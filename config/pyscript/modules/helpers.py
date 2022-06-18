"""helper functions for use across Pyscript"""

# pylint: disable=import-outside-toplevel
from json import loads
from logging import Logger
from socket import gethostname
from typing import Any, Callable, Optional, Tuple, Union
from unittest.mock import MagicMock


def local_setup() -> Tuple[
    Logger, MagicMock, MagicMock, Callable[..., Callable[..., Any]]
]:
    """Helper function for creation of fake/stubbed variables which are automatically
    available to Pyscript

    Returns:
        Logger: a logger
        AsyncMock: an asynchronous mock object
        MagicMock: a synchronous mock object
        function: a function to be used as any decorator - it does nothing
    """
    from logging import DEBUG, getLogger

    from wg_utilities.loggers import add_stream_handler

    def _dummy_decorator(func):  # type: ignore
        """Dummy function for running scripts locally"""
        return func

    _log = getLogger(__name__)
    _log.setLevel(DEBUG)
    add_stream_handler(_log)

    task_mock = MagicMock()
    task_mock.executor = lambda func, *a, **k: func(*a, **k)

    return _log, task_mock, MagicMock(), _dummy_decorator


if gethostname() != "homeassistant":
    log, async_mock, sync_mock, decorator = local_setup()
    pyscript = sync_mock
    pyscript_executor = decorator


def get_secret(
    secret_name: str, *, module: str, default: Optional[str] = None, json: bool = False
) -> Any:
    """Get a secret from Home Assistant (similar to `os.getenv` really)

    Args:
        secret_name (str): the name of the secret to retrieve
        module (str): the name of the module which the secret is for
        default (str): the default value to return
        json (str): boolean for if the secret is JSON to be parsed

    Returns:
        Union[str, dict]: the secret's value
    """

    if gethostname() != "homeassistant":
        from os import getenv

        secret_value = getenv(
            f"{module.upper()}_{secret_name.upper()}", default=default
        )
    else:
        secret_value = (
            pyscript.config.get("apps", {}).get(module, {}).get(secret_name, default)
        )

    if json and isinstance(secret_value, (str, bytes)):
        return loads(secret_value)

    return secret_value


@pyscript_executor
def write_file(
    path: str,
    content: Union[bytes, str],
    mode: str = "wb",
    encoding: Optional[str] = "utf-8",
) -> None:
    """Write a file to local storage

    Args:
        path (str): the file path to be written to
        content (Union[bytes, str]): the content to write to the file
        mode (str): the mode to open the file with
        encoding (Union[None, str]): the type of encoding to use on the file
    """
    with open(path, mode=mode, encoding=encoding) as fout:
        fout.write(content)
