#!/usr/bin/python3
"""
    Module containing function print_square
"""


def print_square(size):
    """Prints in stdout a square with the character #
    Args:
        size (int): the square size
    Returns: nothing
    """
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")

    if size == 0:
        print()
    else:
        for w in range(size):
            print("#" * size)
