#!/usr/bin/python3
"""Module containing an empty class"""


class Rectangle:
    """Class that defines a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object"""
        self.__width = check_format(width, "width")
        self.__height = check_format(height, "height")
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        self.__width = check_format(value, "width")

    @property
    def height(self):
        """Returns the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        self.__height = check_format(value, "height")

    def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns the square with the character #
        according to his position"""
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s

        for w in range(self.__height):
            if w != 0:
                s += "\n"
            s += (str(self.print_symbol) * self.__width)
        return s

    def __repr__(self):
        """Class official representation (wich can be used with eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletes the class object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return (rect_1, rect_2)[rect_2.area() > rect_1.area()]

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)


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
