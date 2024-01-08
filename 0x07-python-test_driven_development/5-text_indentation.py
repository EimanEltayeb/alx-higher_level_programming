#!/usr/bin/python3
""" prints a text with 2 new lines after certain characters"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in ('.', '?', ':'):
            print(text[i])
            print("")
        else:
            if text[i - 1] in ('.', '?', ':') and text[i] == ' ':
                continue
            else:
                print(text[i], end="")
