#!/usr/bin/python3
""" Unittest for class Square """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """TestSquare class for class Square test"""
    def test_type(self):
        self.assertRaises(TypeError, Square.validate, "width", "5")
        self.assertRaises(TypeError, Square.validate, "x", (5, ))
        self.assertRaises(TypeError, Square.validate, "width", [5])
        self.assertRaises(TypeError, Square.validate, "y", {5})
        self.assertRaises(TypeError, Square, "1", 5)
        self.assertRaises(TypeError, Square, 1, "4")
        self.assertRaises(TypeError, Square, 1, 2, "4")
        # self.assertRaises(TypeError, Square, 1, 2, 3, "4")

    def test_values(self):
        self.assertRaises(ValueError, Square, 0, 1)
        # self.assertRaises(ValueError, Square, 4, 0)
        self.assertRaises(ValueError, Square, -1, 2)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 1, 2, -3)
        # self.assertRaises(ValueError, Square, 1, 2, 3, -4)

    def test_almostequal(self):
        r1 = Square(4, 6, 7, 7)
        self.assertTrue(r1)
        self.assertAlmostEqual(r1.area(), 16)
        r2 = Square(2, 2)
        self.assertTrue(r2)
        self.assertAlmostEqual(r2.area(), 4)
        self.assertEqual(r2.display(), None)
        self.assertEqual(Square(2, 4, 2).display(), None)
        self.assertEqual(Square(2, 4, 2, 1).display(), None)
        self.assertEqual(r2.to_dictionary(), {
            'id': 8, 'size': 2, 'x': 2, 'y': 0
            })
        r2.update()
        self.assertEqual(r2, r2)
        r1.update(89)
        self.assertEqual(r1.to_dictionary(), {
            'id': 89, 'size': 4, 'x': 6, 'y': 7
            })

    def test_true(self):
        self.assertTrue(Square(1, 2, 3))
        self.assertTrue(Square(1, 2, 3, 4))
