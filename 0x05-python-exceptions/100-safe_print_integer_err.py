#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as vaerr:
        print(f"Exception: {vaerr}", file=stderr)
        return False
    except TypeError as tyerr:
        print(f"Exception: {tyerr}", file=stderr)
        return False
    return True
