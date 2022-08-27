#!/usr/bin/python3
def format_tuple(tup):
    n = len(tup)
    if n == 0:
        return (0, 0)
    elif n == 1:
        return (tup[0], 0)
    else:
        return tup


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = format_tuple(tuple_a)
    tuple_b = format_tuple(tuple_b)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
