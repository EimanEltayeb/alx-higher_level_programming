#!/usr/bin/python3
"""test module"""


import unittest


import json

from models.base import Base
class TestBase(unittest.TestCase):
    """ tests different functions in base file"""

    def test_to_json_string(self):
        x = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.assertEqual(Base.to_json_string(x), '{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}')

    


if __name__ == '__main__':
    unittest.main()
