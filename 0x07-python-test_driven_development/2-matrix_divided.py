#!/usr/bin/python3
""" this module divide elements of a matrix """


def matrix_divided(matrix, div):
    """ divide elements of matrix
    """

    if not all(isinstance(e, (int, float)) for row in matrix for e in row):
        m = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(m)
    a = len(matrix[0])
    for i in range(len(matrix)):
        if a != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(round(matrix[i][j] / div, 2))
        new.append(row)
    return new
