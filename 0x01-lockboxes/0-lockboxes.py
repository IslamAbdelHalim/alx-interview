#!/usr/bin/python3
""" lockboxes problem"""


def canUnlockAll(boxes):
    """
    function to check of all boxes open

    return:
        true if all boxes open
        false if not
    """

    key = [0]
    for i in key:
        for j in boxes[i]:
            if j not in key and j < len(boxes):
                key.append(j)
    if len(key) == len(boxes):
        return True
    return False
