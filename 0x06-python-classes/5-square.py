#!/usr/bin/python3
"""A module containing a class that defines a square"""


class Square:
    """A class that defines a square

    Attributes:
        size (int, optional): square's size
    """

    def __init__(self, size=0):
        """__init__ method doc"""

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of the current square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the current square size to value"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for w in range(self.__size):
                print("#" * self.__size)
