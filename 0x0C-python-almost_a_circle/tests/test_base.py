#!/usr/bin/python3
"""test module"""


import unittest


import json


from models.base import __init__


from models.base import to_json_string


from models.base import save_to_file


from models.base import from_json_string, create, load_from_file


class Test_base(unittest.TestCase):
    """ tests different functions in base file"""


    def test_to_json_string(self):
        self.assertEqual(to_json_string({'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}), {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8})
        self.assertEqual(to_json_string(), "[]")



