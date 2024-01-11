#!/usr/bin/python3
"""module that creat empty class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""import BaseGeometry class """


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """insantation with width and height"""

        super().__init__()
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        return self.__width * self.__height
