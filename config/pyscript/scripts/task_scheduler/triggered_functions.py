"""Module to allow the creation of triggered service calls on the fly"""
from hashlib import md5
from json import dumps
from socket import gethostname
from typing import TYPE_CHECKING, Any, Callable, Optional, TypedDict

from helpers import HAExceptionCatcher
from yaml import safe_load

if gethostname() != "homeassistant":
    from helpers import local_setup  # pylint: disable=ungrouped-imports

    log, task, sync_mock, decorator, decorator_with_args = local_setup()
    persistent_notification = sync_mock
    state = sync_mock
    state_trigger: Callable[[Any], Callable[..., Any]] = decorator_with_args
    service: Any = decorator

TaskType = Optional[Callable[[str, str], None]]


if TYPE_CHECKING:

    class ScheduledTasksInfo(TypedDict):
        """Typing info for the scheduled tasks record"""

        count: int
        repeat_forever: bool
        task: TaskType

    SCHEDULED_TASKS: dict[str, ScheduledTasksInfo]


SCHEDULED_TASKS = {}


@service  # type: ignore[misc]
def create_task() -> None:
    """Factory to create new services which are triggered by state changes

    Variables:
        trigger_entity_id (str): the ID of the entity to watch for state changes
        trigger_state (str): the state which will cause the function to fire
        service_call (str): the service to call upon trigger
        service_kwargs (dict[str, str], optional): the kwargs to pass to the service
            call. Defaults to None.
        repeat_count (int): the number of times to repeat this function. 0 means forever
    """

    with HAExceptionCatcher("task_scheduler", "get_parameters"):
        trigger_entity_id = str(
            state.get("input_text.task_scheduler_trigger_entity_id")
        )
        trigger_state = str(state.get("input_text.task_scheduler_trigger_state"))
        service_call = str(state.get("input_text.task_scheduler_service_call"))
        service_kwargs = safe_load(
            str(state.get("input_text.task_scheduler_service_kwargs"))
        )
        repeat_count = int(state.get("input_text.task_scheduler_repeat_count"))

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

            with HAExceptionCatcher("task_scheduler", f"run.{trigger_entity_id}"):

                domain, entity = service_call.split(".")

                service.call(domain, entity, **service_kwargs)

                persistent_notification.create(
                    title="Scheduled task run",
                    message=f"Service `{service_call}` called with kwargs "
                    f"`{dumps(service_kwargs, indent=2)}`",
                )

            with HAExceptionCatcher("task_scheduler", f"cleanup.{trigger_entity_id}"):

                if not repeat_forever:
                    SCHEDULED_TASKS[task_uuid]["count"] -= 1
                    if SCHEDULED_TASKS[task_uuid]["count"] == 0:
                        del SCHEDULED_TASKS[task_uuid]

                log.info(dumps(SCHEDULED_TASKS, indent=2, default=str))

        return scheduled_task  # type: ignore[no-any-return]

    with HAExceptionCatcher("task_scheduler", "create_task"):
        task_uuid = md5(
            "|".join(
                [trigger_entity_id, service_call, dumps(service_kwargs, sort_keys=True)]
            ).encode()
        ).hexdigest()

        SCHEDULED_TASKS.setdefault(
            task_uuid,
            {
                "count": 0,
                "repeat_forever": (repeat_forever := repeat_count == 0),
                "task": None,
            },
        )

        if not repeat_forever:
            SCHEDULED_TASKS[task_uuid]["count"] += repeat_count

        if SCHEDULED_TASKS[task_uuid]["task"] is None:
            log.info("Creating task for first time!")
            SCHEDULED_TASKS[task_uuid]["task"] = generate_scheduled_task()

        log.info(dumps(SCHEDULED_TASKS, indent=2, default=str))
