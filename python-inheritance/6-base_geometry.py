#!/usr/bin/python3
"""Module that defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise exception because area is not implemented"""
        raise Exception("area() is not implemented")
