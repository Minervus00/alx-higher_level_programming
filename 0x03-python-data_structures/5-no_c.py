#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for w in my_string:
        if w not in "cC":
            new += w
    return new
