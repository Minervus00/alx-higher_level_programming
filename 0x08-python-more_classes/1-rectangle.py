#!/usr/bin/python3
"""Module containing an empty class"""


class Rectangle:
    """Class that defines a Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = check_format(width, "width")
        self.__height = check_format(height, "height")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = check_format(value, "width")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = check_format(value, "height")


def check_format(value, attr):
    """Checks if the value is valid and can be assigned to width or height.
        Return this value if it's the case or raise an error otherwise

        Args:
            value (any type): the value to be checked
    """
    if isinstance(value, int):
        if value < 0:
            raise ValueError(f"{attr} must be >= 0")
        return value
    else:
        raise TypeError(f"{attr} must be an integer")
