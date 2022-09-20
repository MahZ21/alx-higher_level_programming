#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """
            test for when all values of list are int
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4.5]), 4.5)

    def test_empty(self):
        """
            make sure none is returned when list is empty
        """
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """
            Test a list with one elemenr
        """
        self.assertEqual(max_integer([2]), 2)

    def test_types(self):
        """
            Test with the elements that are not numbers
        """
        self.assertRaises(TypeError, max_integer, [1, 2, 3, "4"])
        self.assertRaises(TypeError, max_integer, ["holberton", 2, 3, 4])

    def test_negative(self):
        """
            test for list with negative numbers only
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_onenegative(self):
        """
            test for one negative number in the list
        """
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)

    def test_max_at_biginning(self):
        """
            test if maximum number is at beginning
        """
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)


if __name__ == '__main__':
    unittest.main()
    