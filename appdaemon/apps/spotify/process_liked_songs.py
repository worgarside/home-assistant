"""App to add recently liked songs to dynamic playlists."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from re import compile as compile_regex
from typing import TYPE_CHECKING, Any

from wg_utilities.clients import SpotifyClient

# pylint: disable=no-name-in-module
from appdaemon.plugins.hass.hassapi import Hass  # type: ignore[import]

if TYPE_CHECKING:
    from wg_utilities.clients.spotify import Playlist, Track


DECADE_PATTERN = compile_regex(r"^\d{3}0s$")
_MONTH_LIST = "|".join(
    [datetime.strptime(str(i + 1), "%m").strftime("%B") for i in range(12)]
)
MONTHLY_PATTERN = compile_regex(rf"^({_MONTH_LIST}) '[0-9]{{2}}$")


class ProcessLikedSongs(Hass):  # type: ignore[misc]
    spotify: SpotifyClient

    def initialize(self) -> None:
        """Initialise the app."""
        self.run_every(self.process_liked_songs, "now", 15 * 60)

        client_id = self.args["client_id"]

        self.spotify = SpotifyClient(
            client_id=client_id,
            client_secret=self.args["client_secret"],
            creds_cache_path=Path(
                f"/config/.wg-utilities/oauth_credentials/SpotifyClient/{client_id}.json"
            ),
            use_existing_credentials_only=True,
        )

    def _get_monthly_playlists(self, return_count: int = 12) -> list[Playlist]:
        """Gets all monthly playlists from Spotify (based on name)

        Args:
            return_count (int): the number of playlists to return (ordered by datetime,
            descending)

        Returns:
            List[Playlist]: a list of Playlist instances
        """
        return sorted(
            (
                p
                for p in self.spotify.current_user.playlists
                if MONTHLY_PATTERN.match(p.name)
            ),
            key=lambda playlist: datetime.strptime(playlist.name, "%B '%y"),
        )[-return_count:]

    def _update_dynamic_playlists(
        self,
        recently_liked: list[Track],
        already_processed_tracks: Iterable[Track] | None,
        target_name_func: Callable[[Track], str],
    ) -> dict[Playlist, list[Track]]:
        """Updates any dynamic playlists from a set of tracks and a naming match criteria

        Args:
            recently_liked (List[Track]): a list of recently liked tracks
            already_processed_tracks (Iterable[Track]): tracks which have already been
            processed
            target_name_func (Callable[[Track], str]): a function to derive a target
            playlist from the track's attributes

        Returns:
            dict[Playlist, List[Track]]: a dictionary of all playlists that have been
            updated
        """

        playlist_updates: dict[Playlist, list[Track]] = {}
        for track in deepcopy(recently_liked):
            if (
                already_processed_tracks is None
                or track not in already_processed_tracks
            ):
                self.log("Processing %s", str(track))

                target_playlist_name = target_name_func(track)

                self.log("Target playlist: %s", target_playlist_name)

                target_playlist: Playlist
                for playlist in playlist_updates:
                    if playlist.name == target_playlist_name:
                        target_playlist = playlist
                        self.log("Found existing playlist %s", target_playlist_name)
                        break
                else:
                    target_playlist = self.spotify.current_user.get_playlists_by_name(  # type: ignore[assignment]
                        target_playlist_name
                    ) or self.spotify.create_playlist(
                        name=target_playlist_name,
                        public=False,
                        collaborative=False,
                    )

                playlist_updates.setdefault(target_playlist, []).append(track)

            self.log("Processed %s", str(track))

        for playlist, tracks in playlist_updates.items():
            self.log("Adding %s to %s", ", ".join(map(str, tracks)), playlist.name)
            self.log("Force add: %s", tracks[0].name == "Sunchyme")
            self.spotify.add_tracks_to_playlist(
                tracks,
                playlist,
                update_instance_tracklist=False,
                force_add=tracks[0].name == "Sunchyme",
            )

        return playlist_updates

    def process_liked_songs(self, _: dict[str, Any]) -> None:
        """Calls other functions which process liked songs, to save polling Spotify's API
        twice"""

        recently_liked = self.spotify.current_user.get_recently_liked_tracks(
            day_limit=7
        )

        self.log("Found %s recently liked tracks", len(recently_liked))

        # Monthly updates

        all_monthly_playlist_tracks = set()

        for playlist in (last_3_monthly_playlists := self._get_monthly_playlists(3)):
            all_monthly_playlist_tracks.update(playlist.tracks)

        self.log(
            "Found %s tracks in playlists %s",
            len(all_monthly_playlist_tracks),
            ", ".join([p.name for p in last_3_monthly_playlists]),
        )

        monthly_updates = self._update_dynamic_playlists(
            recently_liked,
            all_monthly_playlist_tracks,
            lambda t: str(t.metadata["saved_at"].strftime("%B '%y")),
        )

        if monthly_updates:
            self.log(
                "%i monthly playlists updated: %s",
                len(monthly_updates),
                ", ".join([p.name for p in monthly_updates]),
            )
        else:
            self.log("No monthly playlists updated")

        # Decade playlists

        decade_updates = self._update_dynamic_playlists(
            recently_liked,
            None,
            lambda t: str(t.release_date.year)[:3] + "0s",
        )

        if monthly_updates:
            self.log(
                "%i decade playlists updated: %s",
                len(decade_updates),
                ", ".join([p.name for p in decade_updates]),
            )
        else:
            self.log("No decade playlists updated")

        # Notifications

        if monthly_updates:
            self.log("Building notification content")
            message = ""

            for playlist, tracks in monthly_updates.items():
                message += f"\n### {playlist.name}\n"
                for track in tracks:
                    message += f"- {track.name}\n"

                    self.log("Sending notification for %s", track.name)

                    self.notify(
                        name="mobile_app_will_s_pixel_6_pro",
                        message=f'"{track.name}" added to {playlist.name}',
                        data={
                            "actions": [
                                {
                                    "action": "ADD_SONG_TO_CHILL_ELECTRONICA",
                                    "title": "Chill Electronica",
                                },
                                {
                                    "action": "ADD_SONG_TO_JAMBOX_JAMS",
                                    "title": "JAMBOX Jams",
                                },
                                {"action": "ADD_SONG_TO_BOTH", "title": "Both"},
                            ]
                        },
                    )

                    self.log("Notification sent")

            self.persistent_notification(
                title="Spotify Playlists Updated", message=message
            )
