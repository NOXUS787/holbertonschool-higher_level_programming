#!/usr/bin/python3
"""Provides a function that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle.

    Each row begins and ends with 1, and every value in between is the
    sum of the two values above it in the previous row.

    Args:
        n: the number of rows to build.

    Returns:
        list: a list of n lists of integers, or an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        previous = triangle[-1]
        row = [1]
        for j in range(len(previous) - 1):
            row.append(previous[j] + previous[j + 1])
        row.append(1)
        triangle.append(row)

    return triangle
