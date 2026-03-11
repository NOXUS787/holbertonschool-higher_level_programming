#!/usr/bin/python3
"""Unittests for max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 9, 3, 4]), 9)

    def test_one_negative(self):
        self.assertEqual(max_integer([-1, 5, 3]), 5)

    def test_all_negative(self):
        self.assertEqual(max_integer([-4, -2, -9]), -2)


if __name__ == "__main__":
    unittest.main()
