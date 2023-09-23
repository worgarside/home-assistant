# pylint: disable=no-name-in-module
"""Get bank account/card balances from TrueLayer."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from wg_utilities.clients import TrueLayerClient
from wg_utilities.clients.truelayer import Account, Bank, Card

from appdaemon.plugins.hass.hassapi import Hass  # type: ignore[import]


class BankBalanceGetter(Hass):  # type: ignore[misc]
    accounts: dict[str, Account]
    bank: Bank
    cards: dict[str, Card]
    client: TrueLayerClient

    def initialize(self) -> None:
        """Initialize the app."""

        self.bank = Bank[self.args["bank"].upper().replace(" ", "_")]

        self.client = TrueLayerClient(
            client_id=self.args["client_id"],
            client_secret=self.args["client_secret"],
            creds_cache_dir=Path("/config/.wg-utilities/oauth_credentials"),
            use_existing_credentials_only=True,
            bank=self.bank,
        )

        self.accounts = {}
        if accounts := self.args.get("account_ids"):
            for account_ref, account_id in accounts.items():
                if account := self.client.get_account_by_id(account_id):
                    self.accounts[account_ref] = account

            if self.accounts:
                self.run_every(self.update_account_balances, "now", 15 * 60)
                self.log("Added callback for account balances")

        self.cards = {}
        if cards := self.args.get("card_ids"):
            for card_ref, card_id in cards.items():
                if card := self.client.get_card_by_id(card_id):
                    self.cards[card_ref] = card

            if self.cards:
                self.run_every(self.update_card_balances, "now", 15 * 60)
                self.log("Added callback for card balances")

        self.register_service(
            f"appdaemon/refresh_{self.bank.lower()}_access_token",
            self.refresh_access_token,
        )

        self.log(
            "Initialized for bank %s, with %i accounts and %i cards",
            self.bank,
            len(accounts),
            len(cards),
        )

    def refresh_access_token(self, _: dict[str, Any]) -> None:
        """Refresh the access token."""

        self.log("Refreshing access token for %s", self.bank)

        self.client.refresh_access_token()
        self.log("Refreshed access token")

    def update_account_balances(self, _: dict[str, Any]) -> None:
        """Loop through the account IDs and retrieve their balances."""

        for account_ref, account in self.accounts.items():
            variable_id = f"var.truelayer_balance_{self.bank.lower()}_{account_ref}"

            self.call_service(
                "var/set",
                entity_id=variable_id,
                value=account.available_balance,
                force_update=True,
            )

        self.log("Updated account balances")

    def update_card_balances(self, _: dict[str, Any]) -> None:
        """Loop through the card IDs and retrieve their balances."""

        for card_ref, card in self.cards.items():
            variable_id = f"var.truelayer_balance_{self.bank.lower()}"

            if card_ref != "no_ref":
                variable_id += f"_{card_ref}"

            self.call_service(
                "var/set",
                entity_id=variable_id,
                value=card.current_balance,
                force_update=True,
            )

        self.log("Updated card balances")
