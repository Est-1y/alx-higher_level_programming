#!/usr/bin/python3

"""
Is_kind_of_class Module
It creates a function that returns true
if a prototype is_kind_of_class(obj)
"""


def is_kind_of_class(obj, a_class):
    """
    A function that check if obj is an instance of a class
    inherited from a_class
    Args:
        obj: object
        a_class: class
    Return: True or False
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
