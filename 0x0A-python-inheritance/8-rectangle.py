#!/usr/bin/python3
"""Module containing class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry for the win"""

    def area(self):
        """area an public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value assuming that name is always a string"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """__init__ document"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


print(issubclass(Rectangle, BaseGeometry))
