#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = -1
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except (ValueError, TypeError):
            i -= 1
            pass
    print()
    return i + 1
