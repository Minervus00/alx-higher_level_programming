#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    print(f"{n} argument", end="")
    if n != 1:
        print("s", end="")
    if n >= 1:
        print(":")
    else:
        print(".")
    for i, j in enumerate(argv[1:]):
        print(f"{i + 1}: {j}")
