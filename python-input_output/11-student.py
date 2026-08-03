#!/usr/bin/python3
"""Defines a Student class that can be serialized to a dictionary and
rebuilt from one, providing a simple serialization mechanism."""


class Student:
    """Represents a student with a first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student with the given names and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance.

        Args:
            attrs: an optional list of strings naming the attributes to
                include. If it is not a list of strings, every attribute
                is returned.

        Returns:
            dict: the requested attributes of the instance.
        """
        if (type(attrs) is list and
                all(type(item) is str for item in attrs)):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace every attribute of the Student instance.

        Args:
            json: a dictionary whose keys are public attribute names and
                whose values are the values to assign to them.
        """
        for key, value in json.items():
            setattr(self, key, value)
