#!/usr/bin/python3
"""
    Module containing function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first name> <last name>

    Args:
        first_name (str): 1st_name
        last_name (str, opt): last_name

    Returns: Nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
