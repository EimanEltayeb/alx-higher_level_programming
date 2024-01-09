#!/usr/bin/python3
""" JSON to python"""


import json


def from_json_string(my_str):
    """ this function returns an object represented in JSON string"""

    return json.loads(my_str)
