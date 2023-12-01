#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        check = 0
        operator = {'+', '-', '*', '/'}
        for op in operator:
            if op == argv[2]:
                check = 1
        if check == 0:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(argv[1])
            b = int(argv[3])
            if argv[2] == '+':
                result = add(a, b)
                print("{0} + {1} = {2}".format(a, b, result))
            elif argv[2] == '-':
                result = sub(a, b)
                print("{0} - {1} = {2}".format(a, b, result))
            elif argv[2] == '*':
                result = mul(a, b)
                print("{0} * {1} = {2}".format(a, b, result))
            elif argv[2] == '/':
                result = div(a, b)
                print("{0} / {1} = {2}".format(a, b, result))
