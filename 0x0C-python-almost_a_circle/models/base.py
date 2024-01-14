#!/usr/bin/python3
"""Module"""


import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @staticmethod
    def save_to_file(cls, list_objs):
        with open("json", "w") as file:
            file.write(cls.to_json_string(list_objs))
            
