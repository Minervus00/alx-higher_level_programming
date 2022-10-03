#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """TestBase class for class Base test"""
    # def test_type(self):
    #     self.assertRaises(TypeError, max_integer, 5)
    #     self.assertRaises(TypeError, max_integer, "5")
    #     self.assertRaises(TypeError, max_integer, True)

    # def test_values(self):
    #     self.assertRaises(ValueError, max_integer, [1, 2, "3", 4])
    #     self.assertRaises(ValueError, max_integer, [1, 2, True, 4])
    #     self.assertRaises(ValueError, max_integer, [1, 2, [3], 4])

    def test_almostequal(self):
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)
        b2 = Base()
        self.assertAlmostEqual(b2.id, 2)
        b3 = Base(7)
        self.assertAlmostEqual(b3.id, 7)
