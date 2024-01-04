#!/usr/bin/python3
"""
This function generates a Pascal's Triangle up to the given number of rows.
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to 'n' rows.

    Args:
    - n: An integer representing the number of rows for Pascal's Triangle.

    Returns:
    - A list of lists representing Pascal's Triangle up to 'n' rows.
    """

    if n <= 0:
        return []

    result = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, len(row) - 1):
                # Calculating elements of the current row based on the previous row's elements
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
        
    return result