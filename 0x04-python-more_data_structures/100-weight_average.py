#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    tot = 0
    num = 0
    for i in my_list:
        tot = tot + i[0] * i[1]
        num = num + i[1]
    return tot / num
