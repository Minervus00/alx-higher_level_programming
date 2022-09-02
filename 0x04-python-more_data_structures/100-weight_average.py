#!/usr/bin/python3
def weight_average(my_list=[]):
    n = len(my_list)
    if n == 0:
        return 0
    som, div = 0, 0
    for i, j in my_list:
        som += (i * j)
        div += j
    return som / div
