#!/usr/bin/python3
"""
this defines pascal triangle that creates lists
"""


def pascal_triangle(q):
    """
    this defines triangle module.
    """
    if q <= 0:
        return []
    temp = []
    l = []
    for index in range(q):
        row = []
        for k in range(index + 1):
            if index == 0 or k == 0 or index == k:
                row.append(1)
            else:
                row.append(m[k] + m[k - 1])
        m = row
        temp.append(row)
    return temp
