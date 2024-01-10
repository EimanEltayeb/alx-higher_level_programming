#!/usr/bin/python3
"""this module contains function print_sorted"""


class MyList(list):
    """class MyList"""

    def __init__(self, my_list=[]):
        """initialization"""

        self.my_list = my_list

    def print_sorted(self):
        """method to print sorted list"""

        x = sorted(self)
        print(x)
