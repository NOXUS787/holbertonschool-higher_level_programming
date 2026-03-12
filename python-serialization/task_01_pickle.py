#!/usr/bin/env python3
"""Module for serializing and deserializing a custom object using pickle"""

import pickle


class CustomObject:
    """Custom class for serialization"""

    def __init__(self, name, age, is_student):
        """Initialize attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes"""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """Serialize the object to a file"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from file"""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except Exception:
            return None
