#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my = my_list.copy()
    my.reverse()
    for i in range(len(my)):
        x = my[i]
        print("{:d}".format(x))
