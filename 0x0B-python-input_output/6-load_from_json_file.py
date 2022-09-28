#!/usr/bin/python3
"""Module containing load_from_json_file function"""
from json import load


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""
    with open(filename, encoding='utf-8') as f:
        return load(f)
