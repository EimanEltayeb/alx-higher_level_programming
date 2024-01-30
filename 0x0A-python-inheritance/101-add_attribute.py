#!/usr/bin/python3
""" module 101-add_attribute.py """


def add_attribute(clas, att, value):
    if not hasattr(clas, att):
        setattr(clas, att, value)
    elif getattr(clas, att) != value:
        raise TypeError("can't add new attribute")
