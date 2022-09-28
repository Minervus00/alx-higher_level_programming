#!/usr/bin/python3
"""Module containing append_write function"""
from json import loads


def from_json_string(my_str):
    """returns an object (Python data structure) represented by
    a JSON string"""
    return loads(my_str)
