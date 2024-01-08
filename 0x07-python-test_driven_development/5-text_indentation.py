#!/usr/bin/python3
""" prints a text with 2 new lines after certain characters"""


def text_indentation(text):
    """ prints a text with 2 new lines after certain characters"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_line = True
    for i in range(len(text)):
        if text[i] in ('.', '?', ':'):
            print(text[i])
            print("")
            new_line = True
        elif new_line and text[i] == ' ':
            continue
        else:
            print(text[i], end="")
            new_line = False
