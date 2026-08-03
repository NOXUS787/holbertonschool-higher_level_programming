#!/usr/bin/python3
"""This module supplies one function, print_square.

It prints a square of a given size using the # character.
"""


def print_square(size):
    """Print a square of # characters with sides of the given size.

    Raises a TypeError if size is not an integer and a ValueError if it
    is negative.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
