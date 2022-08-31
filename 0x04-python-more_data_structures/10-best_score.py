#!/usr/bin/python3
def best_score(a_dictionary):
    key = None
    maxi = -1
    if a_dictionary is not None:
        for name, score in a_dictionary.items():
            if score > maxi:
                key, maxi = name, score
    return key
