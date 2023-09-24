"""Get bank account/card balances from TrueLayer."""
from __future__ import annotations

from collections.abc import Callable
from enum import StrEnum
from json import dumps
from pathlib import Path
from typing import Any, Literal, overload

from wg_utilities.clients import TrueLayerClient
from wg_utilities.clients.truelayer import Account, Bank, Card

# pylint: disable=no-name-in-module
from appdaemon.plugins.hass.hassapi import Hass  # type: ignore[import]


class EntityType(StrEnum):
    """The type of entity."""

    ACCOUNT = "account"
    CARD = "card"


class BankBalanceGetter(Hass):  # type: ignore[misc]
    bank: Bank
    client: TrueLayerClient
    entities: dict[EntityType, dict[str, Account] | dict[str, Card]]

    def initialize(self) -> None:
        """Initialize the app."""

        self.bank = Bank[self.args["bank_ref"].upper().replace(" ", "_")]

        self.client = TrueLayerClient(
            client_id=self.args["client_id"],
            client_secret=self.args["client_secret"],
            creds_cache_dir=Path("/config/.wg-utilities/oauth_credentials"),
            use_existing_credentials_only=True,
            bank=self.bank,
        )

        self.entities = {}
        for entity_type in EntityType:
            self._initialize_entities(entity_type)

        self.log(dumps(self.entities, default=str))

        self.register_service(
            f"appdaemon/refresh_{self.bank.lower()}_access_token",
            self.refresh_access_token,
        )

        self.log(
            "Initialized for bank %s, with %i accounts and %i cards",
            self.bank,
            len(self.entities[EntityType.ACCOUNT]),
            len(self.entities[EntityType.CARD]),
        )

    def _callback_factory(
        self, entity_key: EntityType
    ) -> Callable[[dict[str, Any]], None]:
        """Return a callback to update the entity balances."""

        def update_entity_balances(_: dict[str, Any]) -> None:
            """Loop through the account/card IDs and retrieve their balances."""

            for entity_ref, entity in self.entities[entity_key].items():
                variable_id = f"var.truelayer_balance_{self.bank.lower()}"

                if entity_ref != "no_ref":
                    variable_id += f"_{entity_ref}"

                self.call_service(
                    "var/set",
                    entity_id=variable_id,
                    value=entity.available_balance
                    if entity_key == EntityType.ACCOUNT
                    else entity.current_balance,
                    force_update=True,
                )

            self.log(
                "Updated entity balances: %s",
                ", ".join(self.entities[entity_key].keys()),
            )

        return update_entity_balances

    @overload
    def _initialize_entities(
        self,
        entity_type: Literal[EntityType.ACCOUNT],
    ) -> dict[str, Account]:
        ...

    @overload
    def _initialize_entities(
        self,
        entity_type: Literal[EntityType.CARD],
    ) -> dict[str, Card]:
        ...

    @overload
    def _initialize_entities(
        self,
        entity_type: EntityType,
    ) -> dict[str, Account] | dict[str, Card]:
        ...

    def _initialize_entities(
        self,
        entity_type: EntityType,
    ) -> dict[str, Account] | dict[str, Card]:
        self.entities.setdefault(entity_type, {})  # type: ignore[arg-type]

        get_entity_by_id = getattr(self.client, f"get_{entity_type}_by_id")

        for entity_ref, entity_id in self.args.get(f"{entity_type}_ids", {}).items():
            if entity := get_entity_by_id(entity_id):
                self.entities[entity_type][entity_ref] = entity
            else:
                self.error(
                    "%s not found for `%s` with ID `%s`",
                    entity_type.title(),
                    entity_ref,
                    entity_id,
                )

        if self.entities[entity_type]:
            callback = self._callback_factory(entity_type)

            self.run_every(callback, "now", 15 * 60)
            self.log(
                "Added callback for %s balances: %s",
                entity_type,
                ", ".join(self.entities[entity_type].keys()),
            )

        return self.entities[entity_type]

    def error(self, msg: str, *args: Any, **kwargs: Any) -> None:
        super().error(f"{self.bank} | {msg}", *args, **kwargs)

    def log(self, msg: str, *args: Any, **kwargs: Any) -> None:
        super().log(f"{self.bank} | {msg}", *args, **kwargs)

    def refresh_access_token(self, _: dict[str, Any]) -> None:
        """Refresh the access token."""

        self.log("Refreshing access token", self.bank)

        self.client.refresh_access_token()
        self.log("Refreshed access token")
