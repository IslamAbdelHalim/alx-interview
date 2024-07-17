#!/usr/bin/python3
"""
Make a function to rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotate it 90 degrees clockwise.
    """
    m = len(matrix)

    for r in range(m):
        for c in range(r):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for r in matrix:
        r.reverse()
