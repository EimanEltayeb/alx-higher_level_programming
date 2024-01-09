#!/usr/bin/python3
""" the module has a function to append text in file"""


def append_write(filename="", text=""):
    """a function to append string at the end of a text file
    and returns the number of characters added
    """

    with open(filename, "a") as file:
        file.write(text)
        return len(text)
