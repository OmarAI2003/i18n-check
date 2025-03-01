# SPDX-License-Identifier: GPL-3.0-or-later
"""
Functions for checking current version of the i18n-check CLI.
"""

from importlib import metadata
from typing import Any, Dict

import requests


def get_local_version() -> str:
    try:
        return metadata.version("i18n-check")

    except metadata.PackageNotFoundError:
        return "Unknown (Not installed via pip)"


def get_latest_version() -> Any:
    try:
        response = requests.get(
            "https://api.github.com/repos/activist-org/i18n-check/releases/latest"
        )
        response_data: Dict[str, Any] = response.json()
        return response_data["name"]

    except Exception:
        return "Unknown (Unable to fetch version)"


def get_version_message() -> str:
    local_version = get_local_version()
    latest_version = get_latest_version()

    if local_version == "Unknown (Not installed via pip)":
        return f"i18n-check {local_version}"
    elif latest_version == "Unknown (Unable to fetch version)":
        return f"i18n-check {latest_version}"

    local_version_clean = local_version.strip()
    latest_version_clean = latest_version.replace("i18n-check", "").strip()

    if local_version_clean == latest_version_clean:
        return f"i18n-check v{local_version_clean}"

    return f"i18n-check v{local_version_clean} (Upgrade available: i18n-check v{latest_version_clean})\nTo update: pip install --upgrade i18n-check"
