#!/usr/bin/env python3
"""VerboseList class that extends Python list"""


class VerboseList(list):
    """List with notifications when modified"""

    def append(self, item):
        """Add item and print notification"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend list and print notification"""
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Remove item and print notification"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item and print notification"""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
