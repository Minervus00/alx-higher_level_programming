#!/usr/bin/python3
"""Module containing the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle docu """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle __init__ docu"""
        self.validate("width", width)
        self.validate("height", height)
        self.validate("x", x)
        self.validate("y", y)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gives the width instance attr value"""
        return self.__width

    @width.setter
    def width(self, val):
        """Sets the width instance attr value"""
        self.validate("width", val)
        self.__width = val

    @property
    def height(self):
        """Gives the height instance attr value"""
        return self.__height

    @height.setter
    def height(self, val):
        """Sets the height instance attr value"""
        self.validate("height", val)
        self.__height = val

    @property
    def x(self):
        """Gives the x instance attr value"""
        return self.__x

    @x.setter
    def x(self, val):
        """Sets the x instance attr value"""
        self.validate("x", val)
        self.__x = val

    @property
    def y(self):
        """Gives the y instance attr value"""
        return self.__y

    @y.setter
    def y(self, val):
        """Sets the y instance attr value"""
        self.validate("y", val)
        self.__y = val

    def validate(self, name, value):
        """Validates value assuming that name is always a string"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if name in ["width", "height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")
        elif name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """ Returns the area """
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for x in range(self.__y):
            print()

        for w in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ String representation """
        stri = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        stri += f" - {self.__width}/{self.__height}"
        return stri

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, val in enumerate(args):
                setattr(self, attrs[i], val)

        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        dic = {
            'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y
            }
        return dic
