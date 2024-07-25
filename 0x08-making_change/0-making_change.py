#!/usr/bin/python3
"""
Greedy and Dynamic programming
"""


def makeChange(coins, total):
    """
        make change coins probelm
    """
    if total <= 0:
        return 0

    coins.sort()
    amount = 0
    total2 = 0
    i = len(coins) - 1
    sub_total = 0

    while i >= 0:
        sub_total = total - total2
        if coins[i] < total and total2 + coins[i] <= total:
            amount += 1
            total2 += coins[i]
        elif sub_total in coins:
            amount += 1
            total2 += sub_total
        else:
            i -= 1

    if total == total2:
        return amount
    else:
        return -1
