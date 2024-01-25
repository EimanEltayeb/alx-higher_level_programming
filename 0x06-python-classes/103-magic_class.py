#!/usr/bin/python3
""" magic class module"""

from math import pi
"""import the pi from math library"""

class MagicClass:
	""" magic class class"""

	def __init__(self, radius):
		"""init method"""
		if type(radius) is not int or type(radius) is not float:
			raise TypeError('radius must be a number')
		self.__radius = radius

	def area(self, radius):
		"""area method"""
		return radius ** 2 * pi

	def circumference(self, radius):
		"""circumference method"""
		return 2 * pi * radius
