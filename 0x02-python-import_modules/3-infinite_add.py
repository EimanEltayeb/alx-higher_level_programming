#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    lenn = len(argv)
    total = 0
    for i in range(1, lenn):
        total += int(argv[i])
    print(total)
