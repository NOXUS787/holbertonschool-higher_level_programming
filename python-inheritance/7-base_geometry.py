#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A class for geometry operations."""

    def area(self):
        """Raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
