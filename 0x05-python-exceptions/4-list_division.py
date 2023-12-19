#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    r = []
    try:
        for x in range(0, list_length):
            try:
                a = my_list_1[x] / my_list_2[x]
                new.append(a)
                r.append(a)
            except ZeroDivisionError:
                new.append(0)
                print("division by 0")
                continue
            except (TypeError, ValueError):
                print("wrong type")
                new.append(0)
                continue
            except IndexError:
                print("out of range")
                new.append(0)
                continue
    finally:
        pass
    return new
