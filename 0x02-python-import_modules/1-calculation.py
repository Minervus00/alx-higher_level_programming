#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    for ope, fct in {"+": add, "-": sub, "*": mul, "/": div}.items():
        print("{} {} {} = {}".format(a, ope, b, fct(a, b)))
