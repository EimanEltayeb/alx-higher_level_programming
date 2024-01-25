#!/usr/bin/python3
""" magic class module"""
from math import pi
"""import the pi from math library"""


class MagicClass:
    """ magic class class"""

    def __init__(self, radius=0):
        if type(radius) != int and type(radius) != float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * pi

    def circumference(self):
        return 2 * pi * self.__radius
