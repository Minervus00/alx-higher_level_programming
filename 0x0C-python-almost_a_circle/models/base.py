#!/usr/bin/python3
"""Module containing the class Base"""
from json import dumps, loads
from os.path import exists


class Base:
    """The class Base documentation"""
    __nb_projects = 0

    def __init__(self, id=None):
        """Base __init__ function doc"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_projects += 1
            self.id = Base.__nb_projects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        which is a list of dictionary representing objects.
        If this list is empty or None, it returns "[]" """
        if list_dictionaries:
            return dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        list_objs is a list of Rectangle or Square objects"""
        if list_objs is None:
            list_objs = []
        list_dic = [obj.to_dictionary() for obj in list_objs]
        fname = f'{cls.__name__}.json'
        with open(fname, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        json_string is a string represention a list of dictionaries"""
        if not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes in the dict already set"""
        obj = cls(5, 5)  # dummy object in order to use update
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        fname = f"{cls.__name__}.json"
        if not exists(fname):
            return []
        with open(fname, 'r', encoding="utf-8") as file:
            json_str = file.read()
        list_dic = cls.from_json_string(json_str)
        list_int = [cls.create(**dic) for dic in list_dic]
        return list_int

    # @classmethod
    # def save_to_file_csv(cls, list_objs):
    #     """"""
    #     pass

    # @classmethod
    # def load_from_file_csv(cls):
    #     """"""
    #     pass
