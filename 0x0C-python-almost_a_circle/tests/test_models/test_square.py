#!/usr/bin/python3
""" test rectangle"""


import unittest

from models.rectangle import validate_h_w, validate_x_y


class TestValidate_h_w(unittest.TestCase):
    """test rectangle"""

    def test_validate_h_w(self, name, value):
        """test validdation function"""

        self.assertRaises(ValueError
