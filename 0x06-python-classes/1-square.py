#!/usr/bin/python3
"""A module containing an class that defines a square
by size a private instance attribute
"""


class Square:
    """An class that defines a square

    Attributes:
        size (int): square's size
    """

    def __init__(self, size):
        self.__size = size
