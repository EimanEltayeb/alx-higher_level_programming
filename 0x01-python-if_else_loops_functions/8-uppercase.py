#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if x >= 'a' and x <= 'z':
            print("{0}".format(chr(ord(x) - 32)), end="")
        else:
            print("{0}".format(chr(ord(x))), end="")
