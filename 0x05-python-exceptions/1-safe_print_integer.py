#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        x = True
    except (ValueError, NameError, TypeError):
        x = False
    return x
