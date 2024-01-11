#!/usr/bin/python3
"""module that creat empty class"""


class BaseGeometry:
    """ BaseGeometry class"""

    def __init__(self):
        """initialising the class"""

        pass

    def area(self):
        """area method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validation method"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
