#!/usr/bin/python3
"""Module containing add_item function"""
from os.path import exists
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """Adds all arguments to a Python list, and then save them to a file"""
    with open("add_item.json", 'a', encoding='utf-8'):
        pass
    if not exists("add_item.json"):
        save_to_json_file([], "add_item.json")

    lst = load_from_json_file("add_item.json")
    lst.extend(argv[1:])
    save_to_json_file(lst, "add_item.json")


add_item()
