#!/usr/bin/python3
""" the module has a function to write in a fiel in JSON"""


import json


def save_to_json_file(my_obj, filename):
    """ the function writes an object to a text file using JSON"""

    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
