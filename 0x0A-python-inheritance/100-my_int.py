#!/usr/bin/python3
"""Module containing class BaseGeometry"""


class MyInt(int):
    """Class MyInt inherits from int"""

    def __init__(self, value):
        if type(value) is not int:
            raise Exception("Value must be an integer")

    def __eq__(self, other):
        """__eq __ documentation"""
        return super().__ne__(other)

    def __ne__(self, other):
        """__ne __ documentation"""
        return super().__eq__(other)
