#!/usr/bin/python3
"""Module containing class BaseGeometry"""


def add_attribute(cls, name, val):
    """Adds a new attribute to an object if it’s possible"""
    tmp = getattr(cls, name, False)
    if not tmp:
        cls.name = val
