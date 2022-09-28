#!/usr/bin/python3
"""Module containing class Student"""


class Student:
    """Defines a student by first_name, last_name and age"""

    def __init__(self, first_name, last_name, age):
        """__init__ docu"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        dic = {}
        if attrs is not None:
            for ky, val in self.__dict__.items():
                if ky in attrs:
                    dic[ky] = val
            return dic
        return self.__dict__
