#!/usr/bin/python3
""" lockboxes problem"""


def canUnlockAll(boxes):
    """
    function to check of all boxes open

    return:
        true if all boxes open
        false if not
    """

    for idx in range(len(boxes) - 1):
        if len(boxes[idx]) == 0:
            return False
    
    return True
