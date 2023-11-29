#!/usr/bin/python3
def uppercase(str):
    for x in str:
        print("{0}".format(chr(ord(x) - 32) if 'a' <= x <= 'z' else x), end="")
    print("{0}".format(""))
