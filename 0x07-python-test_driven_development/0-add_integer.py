#!/usr/bin/python3
"""
This module return the sum of two int or float numbers
"""


def add_integer(a, b=98):
    """
    this is the addition function
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, bool):
        raise TypeError("a must be an integer")
    if isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
