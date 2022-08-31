#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    util = list(a_dictionary.items())[:]
    for i, j in util:
        if j == value:
            del a_dictionary[i]
    return a_dictionary
