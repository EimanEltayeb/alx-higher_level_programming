#!/usr/bin/python3
def pow(a, b):
    x = 1
    for i in range(0, b):
        if b >= 0:
            x = x * a
        else:
            x = x / a
    return (x)
