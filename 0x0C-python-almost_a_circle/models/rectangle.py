#!/usr/bin/python3
"""module"""


Base = __import('base').Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

   @property
   def height(self):
       return self.__height
   @property
   def x(self):
       return self.__x
   @property
   def y(self):
       return self.__y
