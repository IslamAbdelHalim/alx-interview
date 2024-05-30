#!/usr/bin/python3
"""
This function to apply Pascal's Triangle
"""


def pascal_triangle(n):
    """
    This function to implement Pascal algorithm

    n:
        the length of triangle

    return:
        list of list of integers
    """

    if n <= 0:
        return []

    pascal_list = [[1]]
    idx = 0

    while idx < n - 1:
        new_list = [1]
        if len(pascal_list) > 1:
            for i in range(len(pascal_list[idx]) - 1):
                num = pascal_list[idx][i] + pascal_list[idx][i+1]
                new_list.append(num)
        new_list.append(1)
        pascal_list.append(new_list)
        idx += 1
    return pascal_list
