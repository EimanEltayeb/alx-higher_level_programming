#!/usr/bin/python3
for n in range(122,96,-1):
    if n % 2 == 0:
        char = chr(n)
    else:
        char = chr(n - 32)
    print("{0}".format(char), end="")

