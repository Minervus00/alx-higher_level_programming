#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ""
    for i, j in enumerate(str):
        if i != n:
            cpy += j
    return cpy
