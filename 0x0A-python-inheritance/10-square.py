#!/usr/bin/python3
""" module that has square class"""


Rectangle = __import__('9-rectangle').Rectangle

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Square(Rectangle):
    """ class that inherits from Rectangle class"""

    def __init__(self, size):
        self.__size = size
        self.__width = size
        self.__height = size
        super().__init__(size, size)
        super().integer_validator("size", size)

    def area(self):
        """area method: calculates the square's area"""

        return self.__size ** 2
