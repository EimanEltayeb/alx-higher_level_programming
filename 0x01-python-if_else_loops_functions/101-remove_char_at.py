#!/usr/bin/python3
def remove_char_at(str, n):
    x = len(str)
    strn = ""
    if n >= x or n < 0:
        return (str)
    for i in range(0, n):
        strn = strn + str[i]
    for i in range(n + 1, x):
        strn = strn + str[i]
    return (strn)
