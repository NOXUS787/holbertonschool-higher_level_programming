#!/usr/bin/env python3
"""CountedIterator class"""


class CountedIterator:
    """Iterator that counts how many items were iterated"""

    def __init__(self, iterable):
        """Initialize iterator and counter"""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator itself"""
        return self

    def __next__(self):
        """Return next item and increment counter"""
        item = next(self.iterator)  # may raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """Return number of iterated items"""
        return self.count
