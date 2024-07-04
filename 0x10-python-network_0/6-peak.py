#!/usr/bin/python3

"""
finding a peak in alist of unsorted integers.
"""


def find_peak(list_of_integers):
    """finding peak function
    """
    # checking list.
    if not list_of_integers:
        return None

    # initializing indeces.
    low, high = 0, len(list_of_integers) - 1

    # loop.
    while low < high:
        # calculating index.
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # updating mid
            high = mid
        else:
            # updating.
            low = mid + 1

    # returning elements
    return list_of_integers[low]
