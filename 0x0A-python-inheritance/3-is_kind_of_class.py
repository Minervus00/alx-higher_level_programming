#!/usr/bin/python3
"""Module containing is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class"""
    return isinstance(type(obj), a_class) or issubclass(type(obj), a_class)
