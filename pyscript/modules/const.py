"""Constants for the Pyscript integration."""
from __future__ import annotations

from os import environ

OAUTH_CREDS_CACHE_DIR = "/config/.wg-utilities/oauth_credentials"

environ["WG_UTILITIES_CREDS_CACHE_DIR"] = str(OAUTH_CREDS_CACHE_DIR)
