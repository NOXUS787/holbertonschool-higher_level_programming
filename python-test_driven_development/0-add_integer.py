#!/usr/bin/python3
"""This module supplies one function, add_integer.

It adds two numbers together after validating that both are integers
or floats, casting any float down to an integer before the addition.
"""


def add_integer(a, b=98):
    """Return the sum of a and b, both cast to integers.

    Raises a TypeError if either argument is not an integer or a float.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
