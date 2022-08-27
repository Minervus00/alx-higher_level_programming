#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxi = my_list[0]
    for h in my_list[1:]:
        if h > maxi:
            maxi = h
    return maxi
