"""Return fitness variables from Google Fit API."""

from __future__ import annotations

from pathlib import Path
from typing import Any, ClassVar

from wg_utilities.clients import GoogleFitClient

# pylint: disable=no-name-in-module
from appdaemon.plugins.hass.hassapi import Hass  # type: ignore[import]


class FitnessVariablesGetter(Hass):  # type: ignore[misc]
    client: GoogleFitClient

    VARIABLE_DATA_SOURCE_MAPPING: ClassVar[dict[str, str]] = {
        "var.google_fit_active_minutes": "derived:com.google.active_minutes:com.google.android.gms:merge_active_minutes",  # noqa: E501
        "var.google_fit_calories_expended": "derived:com.google.calories.expended:com.google.android.gms:merge_calories_expended",  # noqa: E501
        "var.google_fit_distance_moved": "derived:com.google.distance.delta:com.google.android.gms:merge_distance_delta",  # noqa: E501
        "var.google_fit_step_count": "derived:com.google.step_count.delta:com.google.android.gms:estimated_steps",  # noqa: E501
        "var.google_fit_weight": "derived:com.google.weight:com.google.android.gms:merge_weight",  # n
    }

    def initialize(self) -> None:
        """Initialize the app."""

        self.client = GoogleFitClient(
            client_id=self.args["client_id"],
            client_secret=self.args["client_secret"],
            creds_cache_dir=Path("/config/.wg-utilities/oauth_credentials"),
            use_existing_credentials_only=True,
        )

        self.run_every(self.update_variables, "now", 15 * 60)

    def update_variables(self, _: dict[str, Any]) -> None:
        """Update the Google Fit variables."""
        for var_name, data_source_id in self.VARIABLE_DATA_SOURCE_MAPPING.items():
            data_source = self.client.get_data_source(data_source_id)

            sum_value = data_source.sum_data_points_in_range()
            if isinstance(sum_value, float):
                sum_value = round(sum_value, 2)

            self.call_service(
                "var/set",
                entity_id=var_name,
                value=sum_value,
                force_update=True,
            )
