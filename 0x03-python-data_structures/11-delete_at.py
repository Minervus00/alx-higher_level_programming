#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    n = len(my_list)
    if 0 <= idx < n:
        return [my_list[x] for x in range(n) if x != idx]
    return my_list
