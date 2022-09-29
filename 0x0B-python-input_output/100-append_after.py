#!/usr/bin/python3
"""Module containing append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string"""
    txt = ""
    with open(filename, encoding='utf-8') as fr:
        line = fr.readline()
        while line != "":
            txt += line
            if search_string in line:
                txt += new_string
            line = fr.readline()

    with open(filename, 'w', encoding='utf-8') as fw:
        fw.write(txt)
