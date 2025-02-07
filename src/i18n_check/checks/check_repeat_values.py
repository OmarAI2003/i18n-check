# SPDX-License-Identifier: GPL-3.0-or-later
"""
Checks if the i18n-src file has repeat string values.
If yes, suggest that they be combined using a `_global` sub key at the lowest matching level of i18n-src.

Usage:
    python src/i18n_check/checks/check_repeat_values.py
"""

from collections import Counter

from i18n_check.utils import (
    read_json_file,  
    en_us_json_file,
    lower_and_remove_punctuation

)

en_us_json_dict = read_json_file(en_us_json_file)

# MARK: Repeat Values

all_json_values = [
    lower_and_remove_punctuation(value=v) for v in list(en_us_json_dict.values())
]

json_repeat_value_counts = {
    k: v for k, v in dict(Counter(all_json_values)).items() if v > 1
}

# MARK: Repeat Values

keys_to_remove = []
for repeat_value in json_repeat_value_counts:
    i18n_keys = [
        k
        for k, v in en_us_json_dict.items()
        if repeat_value == lower_and_remove_punctuation(value=v)
        and k[-len("_lower") :] != "_lower"
    ]

    # Needed as we're removing keys that are set to lowercase above.
    if len(i18n_keys) > 1:
        print(f"\nRepeat value: '{repeat_value}'")
        print(f"Number of instances: : {json_repeat_value_counts[repeat_value]}")
        print(f"Keys: {', '.join(i18n_keys)}")

        common_prefix = ""
        min_key_length = min(len(k) for k in i18n_keys)
        common_character = True
        while common_character:
            for i in range(min_key_length):
                if len({k[i] for k in i18n_keys}) == 1:
                    common_prefix += i18n_keys[0][i]
                else:
                    common_character = False
                    break

            common_character = False

        if common_prefix := ".".join(common_prefix.split(".")[:-1]):
            print(f"Suggested new key: {common_prefix}._global.IDENTIFIER_KEY")
        else:
            print("Suggested new key: _global.IDENTIFIER_KEY")

    else:
        # Remove the key if the repeat is caused by a lowercase word.
        keys_to_remove.append(repeat_value)

for k in keys_to_remove:
    json_repeat_value_counts.pop(k, None)

# MARK: Error Outputs

if json_repeat_value_counts:
    if len(json_repeat_value_counts) == 1:
        value_to_be = "value is"

    else:
        value_to_be = "values are"

    raise ValueError(
        f"\n{len(json_repeat_value_counts)} repeat i18n {value_to_be} present. Please combine given the suggestions above.\n"
    )

else:
    print("\nSuccess: No repeat i18n values found in the en-US source file.\n")
