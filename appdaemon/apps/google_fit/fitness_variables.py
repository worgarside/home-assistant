"""Return fitness variables from Google Fit API."""

from __future__ import annotations

from pathlib import Path
from typing import Any, ClassVar

from wg_utilities.clients import GoogleFitClient

# pylint: disable=no-name-in-module
from appdaemon.plugins.hass.hassapi import Hass  # type: ignore[import]


class FitnessVariablesGetter(Hass):  # type: ignore[misc]
    """Return fitness variables from Google Fit API."""

    client: GoogleFitClient

    VARIABLE_DATA_SOURCE_MAPPING: ClassVar[dict[str, str]] = {
        f"var.google_fit_{var_suffix}": ":".join(
            ["derived", namespace, "com.google.android.gms", operation]
        )
        for var_suffix, namespace, operation in [
            ("active_minutes", "com.google.active_minutes", "merge_active_minutes"),
            (
                "calories_expended",
                "com.google.calories.expended",
                "merge_calories_expended",
            ),
            ("distance_moved", "com.google.distance.delta", "merge_distance_delta"),
            ("step_count", "com.google.step_count.delta", "estimated_steps"),
            ("weight", "com.google.weight", "merge_weight"),
        ]
    }

    def initialize(self) -> None:
        """Initialize the app."""

        self.client = GoogleFitClient(
            client_id=self.args["client_id"],
            client_secret=self.args["client_secret"],
            creds_cache_dir=Path("/config/.wg-utilities/oauth_credentials"),
            use_existing_credentials_only=True,
        )

        self.log("Initialized Google Fit client.")

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

        self.log("Updated Google Fit variables.")
