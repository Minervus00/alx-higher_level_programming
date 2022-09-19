#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger class for testing function max_integer"""
    # def test_type(self):
    #     self.assertRaises(TypeError, max_integer, 5)
    #     self.assertRaises(TypeError, max_integer, "5")
    #     self.assertRaises(TypeError, max_integer, True)

    # def test_values(self):
    #     self.assertRaises(ValueError, max_integer, [1, 2, "3", 4])
    #     self.assertRaises(ValueError, max_integer, [1, 2, True, 4])
    #     self.assertRaises(ValueError, max_integer, [1, 2, [3], 4])

    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 1, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([1, 2, 100, 3, 4]), 100)
        self.assertAlmostEqual(max_integer([11, 2, 3, 4]), 11)
        self.assertAlmostEqual(max_integer([]), None)
