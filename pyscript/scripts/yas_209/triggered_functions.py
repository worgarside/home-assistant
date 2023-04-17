# pylint: disable=missing-function-docstring
"""Functions which are only run on a certain trigger"""
from __future__ import annotations

from collections.abc import Callable
from socket import gethostname
from typing import Any

from helpers import HAExceptionCatcher
from wg_utilities.devices.yamaha_yas_209 import YamahaYas209

MODULE_NAME = "yas_209"

if gethostname() != "homeassistant":
    from helpers import local_setup  # pylint: disable=ungrouped-imports

    log, task, sync_mock, decorator, decorator_with_args = local_setup()
    sensor = sync_mock
    persistent_notification = sync_mock
    notify = sync_mock
    state_trigger: Callable[[Any], Callable[..., Any]] = decorator_with_args
    pyscript_executor: Callable[..., Callable[..., Any]] = decorator
    time_trigger: Callable[[Any], Callable[..., Any]] = decorator_with_args
    event_trigger: Callable[[Any], Callable[..., Any]] = decorator_with_args
    service: Callable[..., Callable[..., Any]] = decorator


PAYLOAD = {
    "state": None,
    "album_art_uri": None,
    "volume_level": None,
    "media_duration": None,
    "media_title": None,
    "media_artist": None,
    "media_album_name": None,
}


YAS_209 = task.executor(
    YamahaYas209, sensor.yas_209_local_ip, start_listener=True, resubscribe_seconds=600
)


@service
def yas_209_mute() -> None:
    with HAExceptionCatcher(MODULE_NAME, "yas_209_mute"):
        task.executor(YAS_209.mute)


@service
def yas_209_next_track() -> None:
    with HAExceptionCatcher(MODULE_NAME, "yas_209_next_track"):
        task.executor(YAS_209.next_track)


@service
def yas_209_pause() -> None:
    with HAExceptionCatcher(MODULE_NAME, "yas_209_pause"):
        task.executor(YAS_209.pause)


@service
def yas_209_play() -> None:
    with HAExceptionCatcher(MODULE_NAME, "yas_209_play"):
        task.executor(YAS_209.play)


@service
def yas_209_play_pause() -> None:
    with HAExceptionCatcher(MODULE_NAME, "yas_209_play_pause"):
        task.executor(YAS_209.play_pause)


@service
def yas_209_previous_track() -> None:
    with HAExceptionCatcher(MODULE_NAME, "yas_209_previous_track"):
        task.executor(YAS_209.previous_track)


@service
def yas_209_set_volume_level(volume_level: float) -> None:
    log.info("Setting volume to %s", volume_level)
    with HAExceptionCatcher(MODULE_NAME, "yas_209_set_volume_level"):
        task.executor(YAS_209.set_volume_level, volume_level)


@service
def yas_209_stop() -> None:
    with HAExceptionCatcher(MODULE_NAME, "yas_209_stop"):
        task.executor(YAS_209.stop)


@service
def yas_209_unmute() -> None:
    with HAExceptionCatcher(MODULE_NAME, "yas_209_unmute"):
        task.executor(YAS_209.unmute)


@service
def yas_209_volume_down() -> None:
    log.info("Volume down")
    with HAExceptionCatcher(MODULE_NAME, "yas_209_volume_down"):
        task.executor(YAS_209.volume_down)


@service
def yas_209_volume_up() -> None:
    log.info("Volume up")
    with HAExceptionCatcher(MODULE_NAME, "yas_209_volume_up"):
        task.executor(YAS_209.volume_up)
