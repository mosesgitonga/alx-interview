#!/usr/bin/python3
"""
This function generates a Pascal's Triangle up to the given number of rows.
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    result = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, len(row) - 1):
                row[j] = result[i - 1][j - 1] + result[i - 1][j - 1]
        result.append(row)
        
    return result