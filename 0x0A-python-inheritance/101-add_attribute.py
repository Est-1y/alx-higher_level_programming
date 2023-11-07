#!/usr/bin/python3

"""
Module to add new attributes to objects if it's possible
this raise exceptions if the object cannot have new attribute
Don't use try or except
"""


def add_attribute(obj, attr, value):
    """
    a funtion that adds attribute if possible.
    Args:
       obj
       name
       value
    Return: error if not possible
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
