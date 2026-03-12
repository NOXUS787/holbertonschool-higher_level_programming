#!/usr/bin/env python3
"""Mixins example with Dragon"""


class SwimMixin:
    """Mixin that adds swimming ability"""

    def swim(self):
        """Swim behavior"""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability"""

    def fly(self):
        """Fly behavior"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon that can swim and fly"""

    def roar(self):
        """Dragon roar"""
        print("The dragon roars!")
