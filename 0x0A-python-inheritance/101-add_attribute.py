#!/usr/bin/python3
""" module 101-add_attribute.py """


def add_attribute(clas, att, value):
    if clas.att is None:
        clas.att = value
    elif clas.att is not None and clas.att != value:
        raise TypeError("can't add new attribute")
