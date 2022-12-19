#!/usr/bin/python3
"""Module for peak finding challaenge"""


def find_peak(list_of_integers):
    """find_peak documentation"""
    intgs = list_of_integers
    if not intgs:
        return None

    if intgs[0] > intgs[1]:
        return intgs[0]

    n = len(intgs)
    if intgs[n - 1] > intgs[n - 2]:
        return intgs[n - 1]

    maxi = max(intgs[0], intgs[n - 1])
    i = 1
    while (i < n - 1):
        if intgs[i - 1] < intgs[i] and intgs[i] > intgs[i + 1]:
            return intgs[i]
        if intgs[i] > maxi:
            maxi = intgs[i]
        i += 1

    return maxi
