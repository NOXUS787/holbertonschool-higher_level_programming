#!/usr/bin/python3
"""This module supplies one function, matrix_divided.

It divides every element of a matrix by a number and returns the result
as a new matrix, leaving the original matrix untouched.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by div.

    Every result is rounded to two decimal places.
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(message)

    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(message)
        for item in row:
            if not isinstance(item, (int, float)) or isinstance(item, bool):
                raise TypeError(message)

    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
