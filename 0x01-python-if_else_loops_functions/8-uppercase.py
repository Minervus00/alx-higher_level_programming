#!/usr/bin/python3
def uppercase(str):
    for c in str:
        num = ord(c)
        if 97 <= num <= 122:
            c = chr(num - 32)
        print("{}".format(c), end="")
    print("{}".format("\n"), end="")
