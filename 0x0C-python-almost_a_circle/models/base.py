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

    @classmethod
    def save_to_file(cls, list_objs):
        dic_list = []
        for ob in list_objs:
            dic_list.append(ob.to_dictionary())
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(cls.to_json_string(dic_list))

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        x = cls(1, 1)
        x.update(**dictionary)
        return x

