#!/usr/bin/python3
""" magic class module"""

from math import pi
"""import the pi from math library"""

class MagicClass:
	""" magic class class"""

	def __init__(self, radius):
		if type(self.radius) != int or type(self.radius) != float:
			raise TypeError('radius must be a number')
		self.__radius = radius

	def area(self, radius):
		return radius ** 2 * pi

	def circumference(self, radius):
		return 2 * pi * radius
