#!/usr/bin/python3
"""Module to find the max integer in a list
"""
import numpy as np


def good_format(matrix, stri):
    """Returns the size if matrix is availabe"""
    if not isinstance(matrix, list):
        raise TypeError(f"{stri} must be a list")
    if matrix in ([], [[]]):
        raise ValueError(f"{stri} can't be empty")
    col = len(matrix[0])
    for line in matrix:
        if not isinstance(line, list):
            raise TypeError(f"{stri} must be a list of lists")

        if len(line) != col:
            raise TypeError(f"each row of {stri} must be of the same size")

        for itm in line:
            if not isinstance(itm, (int, float)):
                raise TypeError(f"{stri} should contain only integers or floats")


def lazy_matrix_mul(m_a, m_b):
    good_format(m_a, "m_a")
    good_format(m_b, "m_b")
    m_a = np.array(m_a)
    m_b = np.array(m_b)
    return np.dot(m_a, m_b)
