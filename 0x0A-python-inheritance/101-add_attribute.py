#!/usr/bin/python3
"""Module containing class BaseGeometry"""


def add_attribute(cls, name, val):
    """Adds a new attribute to an object if it’s possible"""
    if not hasattr(cls, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(cls, name, val)
