"""Updater script for Google Fit variables"""
from __future__ import annotations

from collections.abc import Callable
from socket import gethostname
from typing import Any

from helpers import HAExceptionCatcher
from wg_utilities.clients.google_fit import GoogleFitClient

MODULE_NAME = "google_fit"

if gethostname() != "homeassistant":
    from helpers import local_setup  # pylint: disable=ungrouped-imports

    log, async_mock, sync_mock, decorator, decorator_with_args = local_setup()
    task = async_mock
    var = sync_mock
    service: Callable[..., Callable[..., Any]] = decorator
    time_trigger: Callable[[Any], Callable[..., Any]] = decorator_with_args


GOOGLE_FIT = task.executor(
    GoogleFitClient,
    "home-assistant-worgarside",
    scopes=[
        "https://www.googleapis.com/auth/fitness.activity.read",
        "https://www.googleapis.com/auth/fitness.body.read",
        "https://www.googleapis.com/auth/fitness.location.read",
        "https://www.googleapis.com/auth/fitness.nutrition.read",
    ],
    creds_cache_path="/config/.credentials/google_api_creds.json",
)

VARIABLE_DATA_SOURCE_MAPPING = {
    "var.google_fit_active_minutes": "derived:com.google.active_minutes:com.google.android.gms:merge_active_minutes",  # pylint: disable=line-too-long  # noqa: E501
    "var.google_fit_calories_expended": "derived:com.google.calories.expended:com.google.android.gms:merge_calories_expended",  # pylint: disable=line-too-long  # noqa: E501
    "var.google_fit_distance_moved": "derived:com.google.distance.delta:com.google.android.gms:merge_distance_delta",  # pylint: disable=line-too-long  # noqa: E501
    "var.google_fit_step_count": "derived:com.google.step_count.delta:com.google.android.gms:estimated_steps",  # pylint: disable=line-too-long  # noqa: E501
    "var.google_fit_weight": "derived:com.google.weight:com.google.android.gms:merge_weight",  # pylint: disable=line-too-long  # noqa: E501
}


@time_trigger("cron(*/5 * * * *)")
def update_google_fit_variables() -> None:
    """Updates a set of Google Fit variables, as defined in
    `VARIABLE_DATA_SOURCE_MAPPING`
    """
    with HAExceptionCatcher(MODULE_NAME, "update_google_fit_variables"):
        for var_name, data_source_id in VARIABLE_DATA_SOURCE_MAPPING.items():
            try:
                data_source = task.executor(GOOGLE_FIT.get_data_source, data_source_id)
                log.info("Updating %s with sum from `%s`", var_name, data_source_id)

                sum_value = task.executor(data_source.sum_data_points_in_range)
                if isinstance(sum_value, float):
                    sum_value = round(sum_value, 2)

                var.set(
                    entity_id=var_name,
                    value=sum_value,
                    force_update=True,
                )
            except Exception as exc:  # pylint: disable=broad-except
                log.error(
                    "Unable to update variable `%s`: %s - %s",
                    var_name,
                    type(exc).__name__,
                    str(exc),
                )
                var.set(entity_id=var_name, value="unknown", force_update=True)
