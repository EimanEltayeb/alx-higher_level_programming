#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        x = number % 10
        print(x)
        return (x)
    else:
        x = (-1 * number) % 10
        print(x)
        return (x)
