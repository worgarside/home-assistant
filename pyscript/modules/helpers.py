"""helper functions for use across Pyscript"""
from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from json import loads
from logging import DEBUG, INFO, Logger, getLogger
from socket import gethostname
from types import TracebackType
from typing import Any, TypeVar
from unittest.mock import MagicMock

from const import OAUTH_CREDS_CACHE_DIR
from dotenv import load_dotenv
from wg_utilities.clients import (
    GoogleFitClient,
    MonzoClient,
    SpotifyClient,
    TrueLayerClient,
)
from wg_utilities.loggers import add_warehouse_handler

load_dotenv()


LOGGER = getLogger(__name__)
LOGGER.setLevel(DEBUG)
add_warehouse_handler(
    LOGGER,
    level=INFO,
    warehouse_port=8002,
    allow_connection_errors=True,
    pyscript_task_executor=task.executor,  # type: ignore[has-type,used-before-def]  # noqa: F821
)


class HAExceptionCatcher:
    """Custom class for catching any exception which Pyscript throws. Exceptions are
    sent to the RSS log feed for HA-internal logging

    Args:
        module_name (str): the name of the module which the exception has come from
        func_name (str): the name of the function which the exception has come from
    """

    def __init__(self, module_name: str, func_name: str | None = None):
        self.module_name = module_name
        self.func_name = func_name

    def __enter__(self) -> HAExceptionCatcher:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if exc_type and exc_val and exc_tb:
            LOGGER.exception(
                "Unexpected exception in %s.%s",
                self.module_name,
                self.func_name or "<unknown>",
                exc_info=(exc_type, exc_val, exc_tb),
            )


# pylint: disable=import-outside-toplevel
def local_setup() -> (
    tuple[
        Logger,
        MagicMock,
        MagicMock,
        Callable[..., Callable[..., Any]],
        Callable[[Any], Callable[..., Any]],
    ]
):
    """Helper function for creation of fake/stubbed variables which are automatically
    available to Pyscript

    Returns:
        Logger: a logger
        AsyncMock: an asynchronous mock object
        MagicMock: a synchronous mock object
        function: a function to be used as any decorator - it does nothing
    """

    from wg_utilities.loggers import add_stream_handler

    def _simple_decorator(func: Callable[[Any], Any]) -> Callable[[Any, Any], Any]:
        """Dummy function for running scripts locally"""

        @wraps(func)
        def _worker(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        return _worker

    # pylint: disable=unused-argument
    def _decorator_with_args(*args: Any, **kwargs: Any) -> Any:
        return _simple_decorator

    _log = getLogger("custom_components.pyscript.LOCAL_STUB")
    _log.setLevel(DEBUG)
    add_stream_handler(_log)

    task_mock = MagicMock()
    task_mock.executor = lambda func, *a, **k: func(*a, **k)

    return _log, task_mock, MagicMock(), _simple_decorator, _decorator_with_args


if gethostname() != "homeassistant":
    log, task, sync_mock, decorator, _ = local_setup()
    pyscript = sync_mock
    pyscript_executor = decorator
    persistent_notification = sync_mock


def get_secret(
    secret_name: str, *, module: str, default: str | None = None, json: bool = False
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
    content: bytes | str,
    mode: str = "wb",
    encoding: str | None = "utf-8",
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


T = TypeVar("T", TrueLayerClient, SpotifyClient, GoogleFitClient, MonzoClient)


def instantiate_client(
    client_class: type[T],
    module_name: str,
    redirect_uri_override: str | None = None,
    **extra_kwargs: Any,
) -> T:
    """Instantiate an OAuthClient subclass with the appropriate credentials.

    Args:
        client_class (type[OAuthClient]): the OAuthClient subclass to instantiate
        module_name (str): the name of the module which the client is for
        extra_kwargs (Any): any extra keyword arguments to pass to the client
        redirect_uri_override (str): the redirect URI to use for the client

    Returns:
        OAuthClient: the instantiated OAuthClient
    """

    client_class.DEFAULT_CACHE_DIR = OAUTH_CREDS_CACHE_DIR

    client_id = get_secret("client_id", module=module_name)
    client_secret = get_secret("client_secret", module=module_name)

    if not (client_id and client_secret):
        msg = (
            f"Error creating {client_class.__name__}: both client ID"
            f" {'' if client_id else '(missing) '}and secret"
            f" {'' if client_secret else '(missing) '}must be provided."
        )

        LOGGER.error(msg)
        raise ValueError(msg)

    try:
        client = task.executor(
            client_class,
            client_id=client_id,
            client_secret=client_secret,
            oauth_redirect_uri_override=redirect_uri_override,
            use_existing_credentials_only=True,
            **extra_kwargs,
        )  # type: T
    except Exception as exc:
        LOGGER.exception(
            "Error creating %s: %s - %s", client_class.__name__, type(exc).__name__, exc
        )
        raise exc

    assert client.DEFAULT_CACHE_DIR == OAUTH_CREDS_CACHE_DIR
    assert client.creds_cache_path.is_file(), str(client.creds_cache_path)

    client.headless_auth_link_callback = None

    LOGGER.info(
        "Instantiated client for `%s`. Creds cache path: `%s`",
        module_name,
        client.creds_cache_path,
    )

    return client
