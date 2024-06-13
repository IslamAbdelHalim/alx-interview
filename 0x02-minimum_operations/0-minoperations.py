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

    factor = 2
    op = 0

    while n > 1:
        while n % factor == 0:
            op += factor
            n //= factor
        factor += 1
        
    return op
