#!/usr/bin/python3
"""
    Module containing function text_indentation
"""

def text_indentation(text):
    """ Function that prints a text with 2 new lines after
     each of these characters: ., ? and :
    Args:
        text (str): the text
    Returns: nothing """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    x = 0
    while True:
        try:
            a = text[x]
        except Exception:
            break
        print(a, end="")
        if a in [".", "?", ":"]:
            print("\n")
            x += 1
        x += 1
