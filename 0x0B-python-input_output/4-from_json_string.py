#!/usr/bin/python3
"""
this contains the from_json_string function.
"""

import json


def from_json_string(my_str):
    """this returns an object presented by JSON string"""
    return json.loads(my_str)
