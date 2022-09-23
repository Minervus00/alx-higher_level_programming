#!/usr/bin/python3
"""Module to find the max integer in a list
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the product of two matrices using numpy"""

    m_a = np.array(m_a)
    m_b = np.array(m_b)
    return np.matmul(m_a, m_b)
