#!/usr/bin/python3
"""
The `5-save_to_json` module
"""

import json


def save_to_json_file(my_obj, filename):
    """Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
