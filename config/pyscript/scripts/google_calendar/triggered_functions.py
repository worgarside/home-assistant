"""Functions which are only run on a certain trigger"""
from datetime import datetime, timedelta
from socket import gethostname
from typing import TYPE_CHECKING

from wg_utilities.clients import GoogleCalendarClient
from wg_utilities.clients.google_calendar import ResponseStatus

if TYPE_CHECKING:
    from wg_utilities.clients.google_calendar import Event

    # noinspection PyUnresolvedReferences
    from typing import List


MODULE_NAME = "google_calendar"

if gethostname() != "homeassistant":
    from helpers import local_setup

    log, task, sync_mock, decorator = local_setup()
    service = decorator
    pyscript_executor = decorator
    time_trigger = decorator

WORK_CLIENT = GoogleCalendarClient(
    "calendar-copier-252518",
    scopes=[
        "https://www.googleapis.com/auth/calendar",
        "https://www.googleapis.com/auth/calendar.events",
    ],
    creds_cache_path="/config/.credentials/google_api_creds.json",
)

PERSONAL_CLIENT = GoogleCalendarClient(
    "home-assistant-worgarside",
    scopes=[
        "https://www.googleapis.com/auth/fitness.activity.read",
        "https://www.googleapis.com/auth/fitness.body.read",
        "https://www.googleapis.com/auth/fitness.location.read",
        "https://www.googleapis.com/auth/fitness.nutrition.read",
        "https://www.googleapis.com/auth/calendar",
        "https://www.googleapis.com/auth/calendar.events",
    ],
    creds_cache_path="/config/.credentials/google_api_creds.json",
)


@pyscript_executor
def get_accepted_work_events(from_datetime, to_datetime):
    """Get a list of the work events which have been accepted

    Args:
        from_datetime (datetime): the lower bound of the range to look for events in
        to_datetime (datetime): the upper bound of the range to look for events in

    Returns:
        List(Event): a list of events which have been accepted
    """
    events = WORK_CLIENT.primary_calendar.get_events(
        from_datetime=from_datetime, to_datetime=to_datetime
    )

    return sorted([e for e in events if e.response_status == ResponseStatus.ACCEPTED])


@pyscript_executor
def get_previously_copied_events(from_datetime, to_datetime):
    """Get a list of events which have previously been copied to my personal calendar

    Args:
        from_datetime (datetime): the lower bound of the range to look for events in
        to_datetime (datetime): the upper bound of the range to look for events in

    Returns:
        List(Event): a list of events which have been previously copied from my work
         calendar
    """
    events = PERSONAL_CLIENT.primary_calendar.get_events(
        from_datetime=from_datetime, to_datetime=to_datetime
    )

    return sorted(
        [
            e
            for e in events
            if (e.description or "").lower().endswith(" - copied from work calendar.")
        ]
    )


def event_in_list(target_event, event_list):
    """Check if an Event is in a list of Events

    Args:
        target_event (Event): the Event we're checking membership for
        event_list (List(Event)): a list to look in

    Returns:
        bool: if the Event has been found
    """
    for event in event_list:
        if all(
            [
                event.summary == target_event.summary,
                event.response_status == target_event.response_status,
                event.start_datetime == target_event.start_datetime,
                event.end_datetime == target_event.end_datetime,
            ]
        ):
            return True

    return False


@service
@time_trigger("cron(*/5 * * * *)")
def copy_events():
    """Copy events from my work calendar to my personal one"""

    description_suffix = datetime.utcnow().strftime(
        "%Y-%m-%d %H:%M:%S - copied from work calendar."
    )

    from_datetime = datetime.utcnow() - timedelta(days=3)
    to_datetime = datetime.utcnow() + timedelta(weeks=4)

    previously_copied_events = get_previously_copied_events(from_datetime, to_datetime)
    accepted_work_events = get_accepted_work_events(from_datetime, to_datetime)

    for work_event in accepted_work_events:
        if not event_in_list(work_event, previously_copied_events):
            log.info("Creating", str(work_event))
            task.executor(
                PERSONAL_CLIENT.create_event,
                summary=work_event.summary,
                start_datetime=work_event.start_datetime,
                end_datetime=work_event.end_datetime,
                tz=work_event.start.get("timeZone"),
                extra_params={
                    "colorId": 8,  # grey
                    "description": work_event.description + "\n" + description_suffix
                    if work_event.description
                    else description_suffix,
                    "location": work_event.location,
                },
            )

    for copied_event in previously_copied_events:
        if not event_in_list(copied_event, accepted_work_events):
            log.info("Deleting", str(copied_event))
            task.executor(copied_event.delete)
