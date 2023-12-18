#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for a in my_list:
        try:
            if i < x:
                print(a, end="")
                i++
            else:
                break
        except IndexError:
            print("\n")
            break
        return i
