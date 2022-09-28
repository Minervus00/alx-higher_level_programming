#!/usr/bin/python3
"""Module containing append_write function"""
from json import dumps


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return dumps(my_obj)
