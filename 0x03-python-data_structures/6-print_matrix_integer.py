#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for x in row:
            print(x, end=(" ", "")[x == row[-1]])
        print()
