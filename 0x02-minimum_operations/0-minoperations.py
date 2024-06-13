#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
        Minimum Operations
    """
    if n <= 1:
        return 0

    h = 1
    past = 0
    op = 0

    while h < n:
        if past < h / 2 and h * 2 < n:
            past = h
            op += 1
        h += past
        op += 1

    return op
