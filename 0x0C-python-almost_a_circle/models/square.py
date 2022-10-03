#!/usr/bin/python3
"""Module containing the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square docu"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square __init__ documentation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation"""
        stri = f"[Square] ({self.id}) {self.x}"
        stri += f"/{self.y} - {self.width}"
        return stri

    @property
    def size(self):
        """Gives the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        args: id, size, x, y"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, val in enumerate(args):
                setattr(self, attrs[i], val)

        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
