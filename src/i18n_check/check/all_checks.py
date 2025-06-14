# SPDX-License-Identifier: GPL-3.0-or-later
"""
Runs all i18n checks for the project.

Examples
--------
Run the following script in terminal:

>>> python3 src/i18n_check/checks/run_i18n_checks.py
"""

from i18n_check.utils import (
    config_invalid_keys_active,
    config_key_identifiers_active,
    config_nested_keys_active,
    config_non_source_keys_active,
    config_repeat_keys_active,
    config_repeat_values_active,
    config_unused_keys_active,
    run_check,
)

# MARK: Run All


def run_all_checks() -> None:
    """
    Run all internationalization (i18n) checks for the project.

    This function executes a series of checks to validate the project's
    internationalization setup, including key validation, usage checks
    and duplicate detection.

    Raises
    ------
    AssertionError
        If any of the i18n checks fail, an assertion error is raised with
        a message indicating that some checks didn't pass.

    Notes
    -----
    The checks performed include:
    - Invalid key detection
    - Key identifier validation
    - Unused key detection
    - Non-source key detection
    - Repeated key detection
    - Repeated value detection
    - Nested key detection
    """
    checks = []
    if config_invalid_keys_active:
        checks.append("invalid_keys.py")

    if config_key_identifiers_active:
        checks.append("key_identifiers.py")

    if config_unused_keys_active:
        checks.append("unused_keys.py")

    if config_non_source_keys_active:
        checks.append("non_source_keys.py")

    if config_repeat_keys_active:
        checks.append("repeat_keys.py")

    if config_repeat_values_active:
        checks.append("repeat_values.py")

    if config_nested_keys_active:
        checks.append("nested_keys.py")

    if not (
        config_invalid_keys_active
        and config_key_identifiers_active
        and config_unused_keys_active
        and config_non_source_keys_active
        and config_repeat_keys_active
        and config_repeat_values_active
        and config_nested_keys_active
    ):
        print(
            "Note: Some checks are not enabled in the .i18n-check.yaml configuration file and will be skipped."
        )

    check_results: list[bool] = []
    check_results.extend(run_check(check) for check in checks)

    assert all(check_results), (
        "\nError: Some i18n checks did not pass. Please see the error messages above."
    )

    print("\nSuccess: All i18n checks have passed!")


# MARK: Main

if __name__ == "__main__":
    run_all_checks()
