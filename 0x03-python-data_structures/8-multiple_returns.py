#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    if x == 0:
        a = None
    else:
        a = sentence[0]
    return (x, a)
