#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    lenn = len(argv) - 1
    if lenn == 0:
        print("{0} arguments.".format(lenn))
    elif lenn == 1:
        print("{0} argument:".format(lenn))
    else:
        print("{0} arguments:".format(lenn))
    if lenn > 0:
        for i in range(1, len(argv)):
            print("{0}: {1}".format(i, argv[i]))
