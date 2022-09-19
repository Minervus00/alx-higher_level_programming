#!/usr/bin/python3
"""
    Module conatining function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix by div

        Args:
            matrix (list[list]): a list of list of integers or floats
            div (int or float): a number

        Returns:
            list[list]: a new matrix
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not (isinstance(matrix, list) and isinstance(matrix[0], list)):
        raise TypeError(msg)

    length = len(matrix[0])
    for line in matrix:
        if not isinstance(line, list):
            raise TypeError(msg)
        if len(line) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for num in line:
            if not isinstance(num, (int, float)):
                raise TypeError(msg)  

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in line] for line in matrix]
