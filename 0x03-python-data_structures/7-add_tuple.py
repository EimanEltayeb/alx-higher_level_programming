#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a0 = 0 if len(tuple_a) == 0 else tuple_a[1]
    a1 = 0 if len(tuple_a) <= 1 else tuple_a[1]
    b0 = 0 if len(tuple_b) == 0 else tuple_b[1]
    b1 = 0 if len(tuple_b) <= 1 else tuple_b[1]
    n_0 = a0 + b0
    n_1 = a1 + b1
    new = (n_0, n_1)
    return new
