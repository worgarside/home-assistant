"""helper functions for use across Pyscript"""
from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timedelta
from functools import wraps
from json import loads
from logging import Logger
from socket import gethostname
from types import TracebackType
from typing import Any, TypeVar
from unittest.mock import MagicMock

from const import OAUTH_CREDS_CACHE_DIR
from requests import post
from wg_utilities.clients import GoogleFitClient, SpotifyClient, TrueLayerClient


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
        exc_type: type[type] | None,
        exc_val: Exception | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if exc_type is not None:
            task.executor(
                post,
                "http://homeassistant.local:8001/log/error",
                data=f"{exc_type.__name__} in `{self.module_name}"
                f"{f'.{self.func_name}' if self.func_name is not None else ''}`: "
                f"{repr(exc_val)}",
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
    from logging import DEBUG, getLogger

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

    _log = getLogger(__name__)
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

    if json and isinstance(secret_value, (str, bytes)):  # noqa: UP038
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


T = TypeVar("T", TrueLayerClient, SpotifyClient, GoogleFitClient)


def generate_oauth_headless_callback(
    cls: type[T],
) -> Callable[[str], None]:
    """Generate a callback function for use with OAuthClient first time logins.

    Args:
        cls (type[OAuthClient]): the OAuthClient class to use

    Returns:
        Callable[[str], None]: the callback function
    """

    def send_auth_link_as_notification(auth_link: str) -> None:
        """Send the auth link as a persistent notification.

        Args:
            auth_link (str): the auth link to send
        """
        persistent_notification.create(
            title=f"OAuth Link for {cls.__name__}",
            message=f"Click [here]({auth_link}) to complete the OAuth code exchange"
            f" process. Link expires at `{datetime.now() + timedelta(minutes=5)}`",
        )

    return send_auth_link_as_notification


@pyscript_executor
def instantiate_client(
    client_class: type[T],
    module_name: str,
    **extra_kwargs: Any,
) -> T:
    """Instantiate an OAuthClient subclass with the appropriate credentials.

    Args:
        client_class (type[OAuthClient]): the OAuthClient subclass to instantiate
        module_name (str): the name of the module which the client is for
        extra_kwargs (Any): any extra keyword arguments to pass to the client

    Returns:
        OAuthClient: the instantiated OAuthClient
    """

    client_class.DEFAULT_CACHE_DIR = OAUTH_CREDS_CACHE_DIR

    client = client_class(
        client_id=get_secret("client_id", module=module_name),
        client_secret=get_secret("client_secret", module=module_name),
        headless_auth_link_callback=generate_oauth_headless_callback(client_class),
        oauth_redirect_uri_override=get_secret("redirect_uri_override", module="oauth"),
        **extra_kwargs,
    )

    if client.access_token_has_expired:
        client.temp_auth_server.port = 5000

    return client
