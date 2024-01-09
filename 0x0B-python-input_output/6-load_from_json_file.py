#!/usr/bin/python3
""" the module has a function that creates an object from a JSON file"""


import json


def load_from_json_file(filename):
    """ a function that creates an object from JSON file"""

    with open(filename, "r") as file:
        return json.loads(file.read)
