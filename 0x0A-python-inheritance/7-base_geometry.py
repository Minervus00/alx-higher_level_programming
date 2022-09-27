#!/usr/bin/python3
"""Module containing class BaseGeometry"""


class BaseGeometry(object):
    """Class BaseGeometry for the win"""

    def area(self):
        """area() an public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value assuming that name is always a string"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
