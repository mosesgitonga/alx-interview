#!/usr/bin/python3
"""
2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotating a 2d matrix 90 degress anti clockwise
    """
    matrix_len = len(matrix)

    for i in range(matrix_len):
        for j in range(i, matrix_len):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_len):
        matrix[i].reverse()
