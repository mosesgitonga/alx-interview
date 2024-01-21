#!/usr/bin/env python3

def minOperations(n):
    mylist = []
    while n != 1:
        for i in range(2, 9):
            if n % i == 0: 
                n = n / i
                mylist.append(i)
    return sum(mylist )