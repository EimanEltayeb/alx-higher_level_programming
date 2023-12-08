#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for x in new:
        a_dictionary[x] *= 2
    return new
