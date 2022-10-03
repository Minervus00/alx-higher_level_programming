#!/usr/bin/python3
""" Unittest for Square.validate([..])
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """TestSquare class for class Square test"""
    def test_type(self):
        self.assertRaises(TypeError, Square.validate, "width", "5")
        self.assertRaises(TypeError, Square.validate, "x", (5, ))
        self.assertRaises(TypeError, Square.validate, "width", [5])
        self.assertRaises(TypeError, Square.validate, "y", {5})

    def test_values(self):
        self.assertRaises(
            ValueError, Square.validate, Square, "width", 0)
        self.assertRaises(
            ValueError, Square.validate, Square, "width", -4)
        self.assertRaises(
            ValueError, Square.validate, Square, "x", -5)
        self.assertRaises(
            ValueError, Square.validate, Square, "y", -2)

    def test_almostequal(self):
        r1 = Square(4, 6, 7, 7)
        self.assertAlmostEqual(r1.area(), 16)
        r2 = Square(5, 3)
        self.assertAlmostEqual(r2.area(), 25)
        self.assertAlmostEqual(str(r2), "[Square] (1) 3/0 - 5")
        self.assertAlmostEqual(str(r1), "[Square] (7) 6/7 - 4")
