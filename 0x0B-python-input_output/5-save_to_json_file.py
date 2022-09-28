#!/usr/bin/python3
"""Module containing save_to_json_file function"""
from json import dump, load


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        dump(my_obj, f)
