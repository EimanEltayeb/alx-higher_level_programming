#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortt = sorted(a_dictionary)
    for i in sortt:
        print("{0}: {1}".format(i, a_dictionary[i]))
