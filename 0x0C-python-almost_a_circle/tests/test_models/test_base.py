#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """TestBase class for class Base test"""
    def test_true(self):
        self.assertTrue(Base.to_json_string([{'id': 12}]))
        self.assertFalse(Base.from_json_string(None))
        self.assertFalse(Base.from_json_string("[]"))
        self.assertTrue(Base.from_json_string('[{"id": 12}]'))

    def test_almostequal(self):
        self.assertAlmostEqual(Base().id, 1)
        self.assertAlmostEqual(Base().id, 2)
        self.assertAlmostEqual(Base(7).id, 7)

    def test_equal(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), "[{\"id\": 12}]")
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{"id": 12}])
