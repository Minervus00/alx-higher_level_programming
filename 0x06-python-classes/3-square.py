#!/usr/bin/python3
"""A module containing an class that defines a square"""


class Square:
    """An class that defines a square

    Attributes:
        size (int, optional): square's size
    """

    def __init__(self, size=0):
        """__init__ method docs"""

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
