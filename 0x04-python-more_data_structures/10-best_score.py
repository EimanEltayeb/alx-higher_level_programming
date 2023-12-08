#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    i = None
    if not a_dictionary:
        return None
    for x in a_dictionary:
        if a_dictionary[x] > best:
            i = x
            best = a_dictionary[x]
    return i
