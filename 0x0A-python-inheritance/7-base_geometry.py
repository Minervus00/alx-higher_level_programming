#!/usr/bin/python3
"""Module containing class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """area() an public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value assuming that name is always a string"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
