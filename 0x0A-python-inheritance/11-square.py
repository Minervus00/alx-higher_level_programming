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
    
    def area(self):
        """ Returns the area """
        return self.__width * self.__height

    def __str__(self):
        """__str __ documentation"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size):
        """__init__ documentation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns the area """
        return self.__size ** 2

    def __str__(self):
        """__str __ documentation"""
        return f"[Square] {self.__size}/{self.__size}"
