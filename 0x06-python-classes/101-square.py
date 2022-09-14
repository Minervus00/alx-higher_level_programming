#!/usr/bin/python3
"""A module containing a class that defines a square"""


class Square:
    """A class that defines a square

    Attributes:
        size (int, optional): square's size
        position (tuple, optional): square position with format (x, y)
            (where x is right oriented (->) and y is down oriented (↓))
    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method doc"""
        self.__size = check_format_for_size(size)
        self.__position = check_format_for_position(position)

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
        self.__size = check_format_for_size(value)

    @property
    def position(self):
        """Returns the position of the current square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the current square position"""
        self.__position = check_format_for_position(value)

    def my_print(self):
        """Prints in stdout the square with the character #
        according to his position"""
        for x in range(self.__position[1]):
            print()

        if self.__size == 0:
            print()
        else:
            for w in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """Prints in stdout the square with the character #
        according to his position"""
        s = ""
        for x in range(self.__position[1]):
            s += "\n"

        if self.__size == 0:
            s += "\n"
        else:
            for w in range(self.__size):
                if w != 0:
                    s += "\n"
                s += " " * self.__position[0]
                s += ("#" * self.__size)
        return s


def check_format_for_size(value):
    """Checks if the value has the required type to be assigned to size.
        Return this value if it's the case or raise an error otherwise

        Args:
            value (any type): the value to be checked
    """
    if isinstance(value, int):
        if value < 0:
            raise ValueError("size must be >= 0")
        return value
    else:
        raise TypeError("size must be an integer")


def check_format_for_position(value):
    """Checks if the value has the required type to be assigned to position.
        Return this value if it's the case or raise an error otherwise

        Args:
            value (any type): the value to be checked
    """
    if isinstance(value, tuple) and len(value) == 2:
        if any(not isinstance(w, int) for w in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        return value
    else:
        raise TypeError("position must be a tuple of 2 positive integers")
