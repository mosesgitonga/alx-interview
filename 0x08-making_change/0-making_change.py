#!/usr/bin/python3
"""
making change
"""


def makeChange(coins, total):
    """
    fewest number of coins to meet a given amount(total)
    """
    if total <= 0:
        return 0
    temp_total = total
    perfectCoins = []
    coins.sort(reverse=True)
    for coin in coins:
        while total >= coin:
            if total - coin >= 0:
                perfectCoins.append(coin)
                pass
            total -= coin

    coin_sum = sum(perfectCoins)
    if coin_sum == temp_total:
        return len(perfectCoins)
    else:
        return -1
