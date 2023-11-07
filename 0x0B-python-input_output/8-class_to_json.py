#!/usr/bin/python3
"""
class_to_json function.
"""


def class_to_json(obj):
    """this returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)"""
    return obj.__dict__
