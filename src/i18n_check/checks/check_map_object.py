# SPDX-License-Identifier: GPL-3.0-or-later
"""
Checks the i18nMap object to make sure that it's in sync with the base localization file.

Usage:
    python3 src/i18n_check/checks/check_map_object.py
"""

import json

from i18n_check.utils import (
    flatten_nested_dict,
    i18n_map_file,
    i18n_src_file,
    read_json_file,
    spdx_license_identifier,
)

# MARK: Load Base i18n

i18n_src_dict = read_json_file(file_path=i18n_src_file)
flat_i18n_src_dict = {k: k for k, _ in i18n_src_dict.items()}

# MARK: Load i18n Map

with open(i18n_map_file, encoding="utf-8") as f:
    i18n_object_list = f.readlines()

    i18n_object_list_with_key_quotes = []
    for i, line in enumerate(i18n_object_list):
        if i != 0 or i != len(i18n_object_list):
            line = line.strip()
            if line and line[0] != '"':
                line = '"' + line.replace(":", '":', 1)
            i18n_object_list_with_key_quotes.append(line)

    i18n_object = (
        "".join(i18n_object_list_with_key_quotes)
        .replace("export const i18nMap = ", "")
        .replace("};", "}")
        .replace('"{', "{")
        .replace('"}', "}")
        .replace(",}", "}")
    )

    if spdx_license_identifier:
        i18n_object = i18n_object.replace('"// SPDX-License-Identifier": ', "").replace(
            spdx_license_identifier, ""
        )

    i18n_object_dict = json.loads(i18n_object)


# MARK: Flatten i18n Obj

flat_i18n_object_dict = flatten_nested_dict(dictionary=i18n_object_dict)

# MARK: Compare Dicts

assert flat_i18n_src_dict == flat_i18n_object_dict, (
    "\ncheck_map_object failure: The current i18nMap object doesn't match the i18n-src file. Please re-generate the i18nMap object.\n"
)

print("check_map_object success: The current i18nMap object matches the i18n-src file.")
