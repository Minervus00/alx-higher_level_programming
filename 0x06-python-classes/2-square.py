#!/usr/bin/python3
"""A module containing an class that defines a square
by size a private instance attribute
"""


class Square:
    """An class that defines a square

    Attributes:
        size (int, optional): square's size
    """

    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
