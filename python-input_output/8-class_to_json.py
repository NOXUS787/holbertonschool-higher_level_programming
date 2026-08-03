#!/usr/bin/python3
"""Provides a function that returns the dictionary description of an
object for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary description of obj with simple data
    structures for JSON serialization.

    Args:
        obj: an instance of a class whose attributes are all
            serializable (list, dictionary, string, integer, boolean).

    Returns:
        dict: a dictionary of the object's instance attributes.
    """
    return obj.__dict__
