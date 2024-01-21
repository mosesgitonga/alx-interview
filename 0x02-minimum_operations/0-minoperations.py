#!/usr/bin/env python3
"""
minimum operations
"""


def minOperations(n: int) -> int:
    """
    find minimum operations needed to result to n
    """

    mylist = []
    i = 2
    while n > 1:
        if n % i == 0:
            n = n // i
            mylist.append(i)
        else:
            i += 1
    return sum(mylist)
