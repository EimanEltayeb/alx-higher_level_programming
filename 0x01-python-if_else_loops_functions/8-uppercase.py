#!/usr/bin/python3
#def uppercase(str):
str = "hello"
for i in range(len(str)):
    if ord(str[i]) > 96 and ord(str[i]) < 123:
        print("{0}".format(chr(ord(str[i]) + 32)), end="")
    else:
        print("{0}".format(chr(ord(str[i]))), end="")
