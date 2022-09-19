#!/usr/bin/python3
"""
    Module conatining function that adds two integers
"""


def add_integer(a, b=98):
    """Function that adds two integers

    Args:
        a (int): 1st int
        b (int, optional): 2nd int
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b
