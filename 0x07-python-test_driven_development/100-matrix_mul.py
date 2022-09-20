#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def good_format(matrix, str):
    """Returns the size if matrix is availabe"""
    if not isinstance(matrix, list):
        raise TypeError(f"{str} must be a list")
    if matrix in ([], [[]]):
        raise ValueError(f"{str} can't be empty")
    col = len(matrix[0])
    lns = 0
    for line in matrix:
        lns += 1
        if not isinstance(line, list):
            raise TypeError(f"{str} must be a list of lists")

        if len(line) != col:
            raise TypeError(f"each row of {str} must be of the same size")

        for itm in line:
            if not isinstance(itm, (int, float)):
                raise TypeError(
                    f"{str} should contain only integers or floats")
    return (lns, col)


def matrix_mul(m_a, m_b):
    """Returns the product of two matrices"""
    a_dim = good_format(m_a, "m_a")
    b_dim = good_format(m_b, "m_b")
    # print(f"{a_dim=} - {b_dim=}")

    if a_dim[1] != b_dim[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    resu = []
    lnx = []
    for i in range(a_dim[0]):
        lnx.clear()
        for j in range(b_dim[1]):
            tmp = 0
            for k in range(a_dim[1]):
                tmp += m_a[i][k] * m_b[k][j]
            lnx.append(tmp)
        resu.append(lnx[:])
    return resu
