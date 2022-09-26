#!/usr/bin/python3
"""Module containing MyList"""


class MyList(list):
    """Class MyList"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
