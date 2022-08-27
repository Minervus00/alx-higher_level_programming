#!/usr/bin/python3
def multiple_returns(sentence):
    leng, first = len(sentence), None
    if leng > 0:
        first = sentence[0]
    return leng, first
