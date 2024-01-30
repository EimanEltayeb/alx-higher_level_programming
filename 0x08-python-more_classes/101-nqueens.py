#!/usr/bin/python3
""" nquwwns """


import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
n = sys.argv[1]
if not isinstance(n, int):
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

