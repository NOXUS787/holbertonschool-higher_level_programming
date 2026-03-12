#!/usr/bin/env python3
"""Shapes with ABC and duck typing"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Return area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle shape"""

    def __init__(self, radius):
        """Initialize circle"""
        self.radius = radius

    def area(self):
        """Return circle area"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return circle perimeter"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape"""

    def __init__(self, width, height):
        """Initialize rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape information using duck typing"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
