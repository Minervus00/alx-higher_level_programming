#!/usr/bin/python3
""" Unittest for Rectangle.validate([..])
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """TestRectangle class for class Rectangle test"""
    def test_type(self):
        self.assertRaises(TypeError, Rectangle.validate, "width", "5")
        self.assertRaises(TypeError, Rectangle.validate, "x", (5, ))
        self.assertRaises(TypeError, Rectangle.validate, "height", [5])
        self.assertRaises(TypeError, Rectangle.validate, "y", {5})

    def test_values(self):
        self.assertRaises(
            ValueError, Rectangle.validate, Rectangle, "width", 0)
        self.assertRaises(
            ValueError, Rectangle.validate, Rectangle, "height", -4)
        self.assertRaises(
            ValueError, Rectangle.validate, Rectangle, "x", -5)
        self.assertRaises(
            ValueError, Rectangle.validate, Rectangle, "y", -2)

    def test_almostequal(self):
        r1 = Rectangle(4, 6, 7, 7)
        self.assertAlmostEqual(r1.area(), 24)
        r2 = Rectangle(5, 3)
        self.assertAlmostEqual(r2.area(), 15)
        self.assertAlmostEqual(str(r2), "[Rectangle] (2) 0/0 - 5/3")
        self.assertAlmostEqual(str(r1), "[Rectangle] (1) 7/7 - 4/6")
