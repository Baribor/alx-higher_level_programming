#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """The unittest class
    """
    def test_len_cannot_be_called_on_argument(self):
        """Test that the argument passed to the function does not
        support the len function"""
        self.assertRaises(TypeError, max_integer, 3)

    def test_only_negative_numbers(self):
        """Test that function works well with negative numbers"""
        self.assertEqual(-1, max_integer([-2, -3, -4, -5, -1]))

    def test_max_at_beginning(self):
        "Test for max at beginning"
        self.assertEqual(4, max_integer([4, 1, 2, 3]))

    def test_max_at_end(self):
        "Test for max at end"
        self.assertEqual(4, max_integer([1, 2, 3, 4]))

    def test_max_at_mid(self):
        "Test for max at mid"
        self.assertEqual(4, max_integer([0, 1, 4, 2, 3]))

    def test_empty_list(self):
        "Test list is empty"
        self.assertEqual(None, max_integer([]))

    def test_one_item_in_list(self):
        "Test only an item in list"
        self.assertEqual(2, max_integer([2]))
