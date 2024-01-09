#!/usr/bin/python3
"""The module reads text file and prints it"""


def read_file(filename=""):
    """read text from file"""

    with open(filename, "r") as file:
        for line in file:
            print(line.rstrip())
