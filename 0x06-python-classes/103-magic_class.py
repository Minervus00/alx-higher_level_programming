#!/usr/bin/python3
"""Module for MagicClass class"""


class MagicClass:
    """A really magic class
    Attributes: radius (int, optional): the circle radius"""
    def __init__(self, radius=0):
        """__init__ function doc"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """computes the area"""
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """computes the circumference"""
        return 2 * math.pi * self._MagicClass__radius
