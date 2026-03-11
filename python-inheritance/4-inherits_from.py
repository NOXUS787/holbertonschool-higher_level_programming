#!/usr/bin/python3
"""Module that checks if object inherits from a class"""


def inherits_from(obj, a_class):
    """Return True if obj is subclass of a_class but not same class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
