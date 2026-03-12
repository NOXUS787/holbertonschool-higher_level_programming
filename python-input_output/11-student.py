#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of Student"""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            result = {}
            for attr in attrs:
                if attr in self.__dict__:
                    result[attr] = self.__dict__[attr]
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of Student instance from dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
