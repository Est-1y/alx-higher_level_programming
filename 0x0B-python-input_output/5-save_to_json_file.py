#!/usr/bin/python3
"""
this contains the save_to_json_fil" function
"""

import json


def save_to_json_file(my_obj, filename):
    """this writes an object to a text file, using JSON presentation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
