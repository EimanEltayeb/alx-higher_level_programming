#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
        print("Inside result: {}".format(c))
    except ZeroDivisionError:
        print("Inside result: None")
        return None
    return c
