#!/usr/bin/python3
""" writes a string to a text file and return charachter number"""


def write_file(filename="", text=""):
    """ writes a string to a text file and return charachter number"""

    with open(filename, "w") as file:
        file.write(text)
        return len(text)
