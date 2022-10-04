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
        self.assertRaises(TypeError, Rectangle, "1", 5)
        self.assertRaises(TypeError, Rectangle, 1, "4")
        self.assertRaises(TypeError, Rectangle, 1, 2, "4")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

    def test_values(self):
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 4, 0)
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

    def test_almostequal(self):
        r1 = Rectangle(4, 6, 7, 7)
        self.assertTrue(r1)
        self.assertAlmostEqual(r1.area(), 24)
        r2 = Rectangle(2, 2)
        self.assertTrue(r2)
        self.assertAlmostEqual(r2.area(), 4)
        self.assertEqual(r2.display(), None)
        self.assertEqual(Rectangle(2, 4, 2).display(), None)
        self.assertEqual(Rectangle(2, 4, 2, 1).display(), None)
        self.assertEqual(r2.to_dictionary(), {
            'id': 4, 'width': 2, 'height': 2, 'x': 0, 'y': 0
            })
        r2.update()
        self.assertEqual(r2, r2)
        r1.update(89)
        self.assertEqual(r1.to_dictionary(), {
            'id': 89, 'width': 4, 'height': 6, 'x': 7, 'y': 7
            })

    def test_true(self):
        self.assertTrue(Rectangle(1, 2, 3))
        self.assertTrue(Rectangle(1, 2, 3, 4, 5))
