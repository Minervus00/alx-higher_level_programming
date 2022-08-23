#!/usr/bin/python3
for c in "abcdefghijklmnopqrstuvwxyz"[::-1]:
    print(chr(ord(c) - 32) if ord(c) % 2 != 0 else c, end="")
