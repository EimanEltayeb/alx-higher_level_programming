#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for a in matrix:
        s = map(lambda x: x ** 2, a)
        new.append(list(s))
    return new
