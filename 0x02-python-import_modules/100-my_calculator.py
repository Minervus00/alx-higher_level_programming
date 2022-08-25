#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    calc = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in calc:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a, b = argv[1], argv[3]
    fct = calc[argv[2]]
    print("{} {} {} = {}".format(a, argv[2], b, fct(a, b)))
