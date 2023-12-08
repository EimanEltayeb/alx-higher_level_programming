#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    summ = 0
    for i in new:
        summ += i
    return summ
