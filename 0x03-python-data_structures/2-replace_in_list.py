#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Substitute element of a list at specific position."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
