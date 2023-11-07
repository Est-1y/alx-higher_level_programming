#!/usr/bin/python3
"""
this contains the function append_wrtie.
"""


def append_write(filename="", text=""):
    """this returns a number of chars appended to filename from text """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
