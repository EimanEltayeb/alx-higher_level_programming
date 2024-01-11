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

        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """insantation with width and height"""

        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
