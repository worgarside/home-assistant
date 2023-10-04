"""App to add recently liked tracks to dynamic playlists."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from json import dumps
from pathlib import Path
from re import compile as compile_regex
from re import sub
from typing import TYPE_CHECKING, Any, Literal, Self

from wg_utilities.clients import SpotifyClient
from wg_utilities.loggers import add_warehouse_handler

# pylint: disable=no-name-in-module
from appdaemon.plugins.hass.hassapi import Hass  # type: ignore[import]

if TYPE_CHECKING:
    from wg_utilities.clients.spotify import Playlist, Track


DECADE_PATTERN = compile_regex(r"^\d{3}0s$")
_MONTH_LIST = "|".join(
    [datetime.strptime(str(i + 1), "%m").strftime("%B") for i in range(12)]
)
MONTHLY_PATTERN = compile_regex(rf"^({_MONTH_LIST}) '[0-9]{{2}}$")


class ActionablePlaylist(StrEnum):
    action_phrase: str
    slug: str

    CHILL_ELECTRONICA = "Chill Electronica"
    JAMBOX_JAMS = "JAMBOX Jams"

    def __new__(cls, *values: str) -> Self:
        value = str(*values)

        member = str.__new__(cls, value)
        member._value_ = value

        _slug = sub(r"[^\w\s]", "", value.lower().replace(" ", "_"))

        member.slug = _slug
        member.action_phrase = f"ADD_TRACK_TO_{_slug.upper()}"

        return member


class SpotifyTrackProcessor(Hass):  # type: ignore[misc]
    playlists: dict[str, Playlist]
    spotify: SpotifyClient

    def initialize(self) -> None:
        """Initialise the app."""

        add_warehouse_handler(self.err)

        self.spotify = SpotifyClient(
            client_id=self.args["client_id"],
            client_secret=self.args["client_secret"],
            creds_cache_dir=Path("/config/.wg-utilities/oauth_credentials"),
            use_existing_credentials_only=True,
        )

        _ = self.spotify.current_user.playlists  # Pre-load playlists

        self.log("Logged in as %s", self.spotify.current_user)

        self.playlists = {
            ActionablePlaylist.CHILL_ELECTRONICA: self.spotify.get_playlist_by_id(
                "2lMx8FU0SeQ7eA5kcMlNpX"
            ),
            ActionablePlaylist.JAMBOX_JAMS: self.spotify.get_playlist_by_id(
                "4Vv023MaZsc8NTWZ4WJvIL"
            ),
            "pixel_now_playing": self.spotify.get_playlist_by_id(
                "7vK46qf4I352doLdlSG9G0"
            ),
        }

        self.run_every(self.process_liked_tracks, "now", 15 * 60)
        self.listen_state(self.process_now_playing, "var.tasker_pixel_now_playing")
        self.listen_state(
            self.update_tempo_variable, "sensor.spotify_will_garside_media_title"
        )
        self.listen_event(self.add_track_to_playlist, "mobile_app_notification_action")

    def add_track_to_playlist(
        self,
        _: Literal["mobile_app_notification_action"],
        data: dict[str, str],
        __: dict[str, str],
    ) -> None:
        """Add a given track to a playlist, triggered from mobile notification

        Args:
            _ (str): the event name
            data (dict[str, str]): the event data
            __: any other kwargs

        Raises:
            Exception: if the desired track can't be found in the recently liked
        """

        action_phrase, track_id = data.get("action", "0:0").split(":")

        if not action_phrase.startswith("ADD_TRACK_TO_"):
            return

        for actionable in ActionablePlaylist:
            if actionable.action_phrase == action_phrase:
                break
        else:
            raise ValueError(f"Unknown action phrase {action_phrase}")

        track = self.spotify.get_track_by_id(track_id)

        self.log("Adding track %s to playlist %s", track, actionable)

        self.spotify.add_tracks_to_playlist([track], self.playlists[actionable])

    def process_liked_tracks(self, _: dict[str, Any]) -> None:
        """Add recently liked tracks to dynamically generated playlists.

        Tracks are added to a playlist for the current month, and a playlist for the
        decade of the track's release date. If the track is already in a playlist, it
        will not be added again.

        One (and only one) notification is also sent per track, to allow for further
        actions to be taken.

        Args:
            _: any kwargs
        """

        recently_liked = self.spotify.current_user.get_recently_liked_tracks(
            day_limit=7
        )

        self.log("Found %s recently liked tracks", len(recently_liked))

        actual_updates = {}
        recently_liked_by_playlist: dict[str, list[Track]] = {}

        for track in recently_liked:
            monthly_playlist_name = track.metadata["saved_at"].strftime("%B '%y")
            decade_playlist_name = str(track.release_date.year)[:3] + "0s"

            recently_liked_by_playlist.setdefault(monthly_playlist_name, []).append(
                track
            )
            recently_liked_by_playlist.setdefault(decade_playlist_name, []).append(
                track
            )

        self.log(
            "Playlists to update: %s", dumps(recently_liked_by_playlist, default=str)
        )

        for target_playlist_name, tracks_to_add in recently_liked_by_playlist.items():
            if not (
                playlist := self.spotify.current_user.get_playlists_by_name(
                    target_playlist_name
                )
            ):
                self.log("Creating playlist %s", target_playlist_name)
                playlist = self.spotify.create_playlist(
                    name=target_playlist_name,
                    public=False,
                    collaborative=False,
                )

            tracks_added = self.spotify.add_tracks_to_playlist(
                tracks_to_add,
                playlist,
            )

            if tracks_added:
                self.log(
                    "Added %s tracks to playlist %s: %s",
                    len(tracks_added),
                    target_playlist_name,
                    ", ".join([f"{t.name!r} by {t.artist}" for t in tracks_added]),
                )
                actual_updates[playlist.name] = tracks_added

        self.log(
            "%i playlists updated: %s",
            len(actual_updates),
            dumps(actual_updates, default=str),
        )

        # Notifications

        if actual_updates:
            message = ""

            notified_tracks = set()

            for playlist_name, tracks in actual_updates.items():
                message += f"\n### {playlist_name}\n"
                for track in tracks:
                    message += f"- {track.name}\n"

                    if track in notified_tracks:
                        continue

                    self.notify(
                        name="mobile_app_will_s_pixel_6_pro",
                        message=f'"{track.name}" added to {playlist_name}',
                        data={
                            "actions": [
                                {
                                    "action": f"{actionable.action_phrase}:{track.id}",
                                    "title": actionable,
                                }
                                for actionable in ActionablePlaylist
                            ]
                        },
                    )

                    self.log("Notification sent for %s", track.name)

                    notified_tracks.add(track)

            self.persistent_notification(
                title="Spotify Playlists Updated", message=message
            )

    def process_now_playing(
        self,
        entity: Literal["var.tasker_pixel_now_playing"],
        attribute: Literal["state"],
        old: str,
        new: str,
        pin_app: bool,
        **kwargs: dict[str, Any],
    ) -> None:
        """Process an update from the Pixel Now Playing Tasker task.

        Args:
            entity (str): the entity that triggered the update
            attribute (str): the attribute that triggered the update
            old (str): the old value
            new (str): the new value, in the format "Track Name by Artist"
            pin_app (bool): whether the app should be pinned
            kwargs (dict[str, Any]): any other kwargs
        """
        _ = entity, old, pin_app, kwargs

        if attribute != "state" or not new:
            return

        matched_track = self.spotify.search(
            (search_term := new.replace(" by ", " ")),
            entity_types=["track"],
            get_best_match_only=True,
        )

        if matched_track is not None:
            self.log(
                "Track found for search term '%s' with ID %s",
                search_term,
                matched_track.id,
            )

            current_track = self.spotify.current_user.current_track

            if current_track is not None and (
                current_track == matched_track
                or (
                    current_track.name == matched_track.name
                    and current_track.artists == matched_track.artists
                )
            ):
                self.log(
                    "Not adding track to Pixel Now Playing playlist, it's currently playing: %s",
                    current_track,
                )
            else:
                self.log(
                    "Adding track to Pixel Now Playing playlist: %s", matched_track
                )
                self.spotify.add_tracks_to_playlist(
                    [matched_track], self.playlists["pixel_now_playing"]
                )
        else:
            self.error("No matching track found for search term '%s'", search_term)

    def update_tempo_variable(
        self,
        entity: Literal["sensor.spotify_will_garside_media_title"],
        attribute: Literal["state"],
        old: str,
        new: str,
        pin_app: bool,
        **kwargs: dict[str, Any],
    ) -> None:
        """Update the tempo variable for a given user.

        Args:
            entity (str): the entity that triggered the update
            attribute (str): the attribute that triggered the update
            old (str): the old value
            new (str): the new value
            pin_app (bool): whether the app should be pinned
            kwargs (dict[str, Any]): any other kwargs
        """

        _ = entity, old, pin_app, kwargs

        if attribute != "state" or not new:
            return

        tempo_variable_name = "var.spotify_tempo_will"

        if new in ("unknown", None, ""):
            self.log(
                "`%s` has state `%s`, setting `%s` to `unknown`",
                entity,
                new,
                tempo_variable_name,
            )
            self.call_service(
                "var/set",
                entity_id=tempo_variable_name,
                value="unknown",
                force_update=True,
            )
        else:
            track_id = self.get_state(
                "media_player.spotify_will_garside", attribute="media_content_id"
            ).replace("spotify:track:", "")

            track = self.spotify.get_track_by_id(track_id)

            self.log(
                "`%s` has state `%s`, setting `%s` to `%i`",
                entity,
                new,
                tempo_variable_name,
                track.tempo,
            )

            self.call_service(
                "var/set",
                entity_id=tempo_variable_name,
                value=track.tempo,
                force_update=True,
            )
