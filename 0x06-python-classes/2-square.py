#!/usr/bin/python3
"""square
"""


class Square:
    """Square class.
    """

    def __init__(self, size=0):
        self.__size = size
        if size % 1 != 0:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
