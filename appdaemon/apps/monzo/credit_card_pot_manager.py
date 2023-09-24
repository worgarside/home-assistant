"""Manage my Monzo pot for credit card payments."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Literal

from wg_utilities.clients import MonzoClient
from wg_utilities.clients.monzo import Pot

# pylint: disable=no-name-in-module
from appdaemon.plugins.hass.hassapi import Hass  # type: ignore[import]


class CreditCardPotManager(Hass):  # type: ignore[misc]
    client: MonzoClient
    credit_card_pot: Pot

    def initialize(self) -> None:
        """Initialize the app."""

        self.client = MonzoClient(
            client_id=self.args["client_id"],
            client_secret=self.args["client_secret"],
            creds_cache_dir=Path("/config/.wg-utilities/oauth_credentials"),
            use_existing_credentials_only=True,
        )

        if not (credit_card_pot := self.client.get_pot_by_name("credit cards")):
            self.error("Could not find credit card pot")
            raise RuntimeError("Could not find credit card pot")

        self.credit_card_pot = credit_card_pot

        self.listen_event(self.top_up_credit_card_pot, "mobile_app_notification_action")

        self.log("Listen event registered for %s", self.credit_card_pot.name)

    def top_up_credit_card_pot(
        self,
        _: Literal["mobile_app_notification_action"],
        data: dict[str, Any],
        __: dict[str, str],
    ) -> None:
        """Top up the credit card pot when a notification action is received."""

        action_phrase, top_up_amount_str = data.get("action", "0:0").split(":")

        if action_phrase != "TOP_UP_CREDIT_CARD_POT":
            return

        top_up_amount = round(float(top_up_amount_str) * 100)

        if not 0 < top_up_amount < 1000 * 100:
            self.error("Invalid top up amount %s", top_up_amount)
            return

        self.client.deposit_into_pot(
            self.credit_card_pot,
            amount_pence=top_up_amount,
            dedupe_id="-".join(
                (
                    self.name,
                    str(top_up_amount),
                    data.get("metadata", {}).get("context", {}).get("id", ""),
                )
            ),
        )

        self.log("Topped up credit card pot by %i", top_up_amount)
