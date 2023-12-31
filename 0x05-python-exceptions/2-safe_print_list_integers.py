#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    num = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
            num += 1
        except (TypeError, ValueError):
            i += 1
            continue
    print("")
    return num
