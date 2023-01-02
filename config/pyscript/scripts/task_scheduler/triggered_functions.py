"""Module to allow the creation of triggered service calls on the fly"""
from __future__ import annotations

from collections.abc import Callable
from hashlib import md5
from json import dumps
from socket import gethostname
from typing import TYPE_CHECKING, Any, Literal, Optional, TypedDict

from helpers import HAExceptionCatcher
from yaml import safe_load

MODULE_NAME = "task_scheduler"

if gethostname() != "homeassistant":
    from helpers import local_setup  # pylint: disable=ungrouped-imports

    log, task, sync_mock, decorator, decorator_with_args = local_setup()
    persistent_notification = sync_mock
    state = sync_mock
    state_trigger: Callable[[Any], Callable[..., Any]] = decorator_with_args
    service: Any = decorator

TaskType = Optional[Callable[[str, str], None]]


if TYPE_CHECKING:

    class ScheduledTaskConfigInfo(TypedDict):
        """Typing info for the `config` field in the scheduled tasks records"""

        repeat_forever: bool
        runs_remaining: int | Literal["∞"]
        service_call: str
        service_kwargs: str
        total_repeat_count: int
        trigger_entity_id: str
        trigger_state: str

    class ScheduledTasksInfo(TypedDict):
        """Typing info for the scheduled tasks record"""

        task: TaskType
        config: ScheduledTaskConfigInfo

    SCHEDULED_TASKS: dict[str, ScheduledTasksInfo]


SCHEDULED_TASKS = {}
MQTT_SENSOR_TOPIC = "/task_scheduler/scheduled_tasks"


def update_sensor() -> None:
    """Update the MQTT sensor `sensor.scheduled_tasks` with the current record"""

    if len(SCHEDULED_TASKS) == 0:
        task_list = []
    else:
        task_list = [task["config"] for task in SCHEDULED_TASKS.values()]

    with HAExceptionCatcher(MODULE_NAME, "update_sensor"):
        service.call(
            "mqtt",
            "publish",
            topic=MQTT_SENSOR_TOPIC,
            payload=dumps({"scheduledTasks": task_list}),
        )


@service  # type: ignore[misc]
def create_task() -> None:
    """Factory to create new services which are triggered by state changes

    Variables:
        trigger_entity_id (str): the ID of the entity to watch for state changes
        trigger_state (str): the state which will cause the function to fire
        service_call (str): the service to call upon trigger
        service_kwargs (dict[str, str], optional): the kwargs to pass to the service
            call. Defaults to None.
        input_repeat_count (int): the number of times to repeat this function. 0 means
            forever
    """

    with HAExceptionCatcher(MODULE_NAME, "get_parameters"):
        trigger_entity_id = str(
            state.get("input_text.task_scheduler_trigger_entity_id")
        )
        trigger_state = str(state.get("input_text.task_scheduler_trigger_state"))
        service_call = str(state.get("input_text.task_scheduler_service_call"))
        service_kwargs = safe_load(
            str(state.get("input_text.task_scheduler_service_kwargs"))
        )
        input_repeat_count = int(state.get("input_text.task_scheduler_repeat_count"))

    def generate_scheduled_task() -> TaskType:
        """Factory to create new services which are triggered by user-defined state
        changes
        """

        @state_trigger(
            f"{trigger_entity_id} == '{trigger_state}'",
        )
        def scheduled_task() -> None:
            """Dynamic service which is triggered by user-defined state changes, to
            allow user defined triggered services to be created on the fly
            """

            with HAExceptionCatcher(MODULE_NAME, f"run.{trigger_entity_id}"):
                domain, entity = service_call.split(".")
                service.call(domain, entity, **service_kwargs)

                persistent_notification.create(
                    title="Scheduled task run",
                    message=f"Service `{service_call}` called with kwargs "
                    f"<pre>{dumps(service_kwargs, indent=2)}</pre>",
                )

            with HAExceptionCatcher(MODULE_NAME, f"cleanup.{trigger_entity_id}"):
                if isinstance(
                    SCHEDULED_TASKS[task_uuid]["config"]["runs_remaining"], int
                ):
                    if SCHEDULED_TASKS[task_uuid]["config"]["repeat_forever"] is True:
                        # Runs remaining is an integer but repeat forever is True
                        raise ValueError(
                            "Invalid config: task is set to repeat forever but"
                            " `runs_remaining` has value "
                            f"{SCHEDULED_TASKS[task_uuid]['config']['runs_remaining']}"
                        )
                elif SCHEDULED_TASKS[task_uuid]["config"]["runs_remaining"] == "∞":
                    if SCHEDULED_TASKS[task_uuid]["config"]["repeat_forever"] is False:
                        # Runs remaining is set to infinity but repeat forever is False
                        raise ValueError(
                            "Invalid config: task is set to not repeat forever but"
                            " `runs_remaining` has value '∞'"
                        )
                else:
                    # Any non-integer value
                    raise ValueError(
                        f"Invalid value for `runs_remaining`:"
                        f" {SCHEDULED_TASKS[task_uuid]['config']['runs_remaining']}"
                    )

                if isinstance(
                    SCHEDULED_TASKS[task_uuid]["config"]["runs_remaining"], int
                ):
                    SCHEDULED_TASKS[task_uuid]["config"][  # type: ignore[operator]
                        "runs_remaining"
                    ] -= 1
                    if SCHEDULED_TASKS[task_uuid]["config"]["runs_remaining"] == 0:
                        del SCHEDULED_TASKS[task_uuid]

                    update_sensor()

                log.info(dumps(SCHEDULED_TASKS, indent=2, default=str))

        return scheduled_task  # type: ignore[no-any-return]

    with HAExceptionCatcher(MODULE_NAME, "create_task"):
        task_uuid = md5(
            "|".join(
                [
                    trigger_entity_id,
                    trigger_state,
                    service_call,
                    dumps(service_kwargs, sort_keys=True),
                ]
            ).encode()
        ).hexdigest()

        if (
            existing_record_config := SCHEDULED_TASKS.get(
                task_uuid, {}  # type: ignore[call-overload]
            ).get("config")
        ) is not None:
            # If this is the second time this task is being scheduled, i.e. updating
            # the config

            if repeat_forever := bool(
                existing_record_config["repeat_forever"] or (input_repeat_count == 0)
            ):
                runs_remaining = "∞"
            elif isinstance(existing_record_config["runs_remaining"], int):
                runs_remaining = int(
                    existing_record_config["runs_remaining"]  # type: ignore[assignment]
                    + input_repeat_count
                )
            else:
                raise ValueError(
                    "Unable to update `runs_remaining` due to existing config values:"
                    f" {dumps(existing_record_config, default=str)}"
                )

            SCHEDULED_TASKS[task_uuid]["config"].update(
                {
                    "repeat_forever": repeat_forever,
                    "runs_remaining": runs_remaining,  # type:ignore[typeddict-item]
                    "total_repeat_count": existing_record_config["total_repeat_count"]
                    + input_repeat_count,
                }
            )
        else:
            SCHEDULED_TASKS[task_uuid] = {
                "task": None,
                "config": {
                    "repeat_forever": input_repeat_count == 0,
                    "runs_remaining": "∞"
                    if input_repeat_count == 0
                    else input_repeat_count,
                    "service_call": service_call,
                    "service_kwargs": dumps(service_kwargs, indent=2),
                    "total_repeat_count": input_repeat_count,
                    "trigger_entity_id": trigger_entity_id,
                    "trigger_state": trigger_state,
                },
            }

        if SCHEDULED_TASKS[task_uuid]["task"] is None:
            log.info("Creating task for first time!")
            SCHEDULED_TASKS[task_uuid]["task"] = generate_scheduled_task()

        update_sensor()
        log.info(dumps(SCHEDULED_TASKS, indent=2, default=str))


# Update (reset) sensor on script load
update_sensor()
