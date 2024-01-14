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
        dic_list = []
        for ob in list_objs:
            dic_list.append(cls.to_json_string(ob.to_dictionary()))
        print(dic_list)
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(str(dic_list))
