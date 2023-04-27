#!/usr/bin/env python3
"""Creating unittests"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any


class TestAccessNestedMap(unittest.TestCase):
    """Testing access nested maps"""

    @parameterized.expand([  # Creating cases to pass to the method
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, value, path, expected) -> Any:
        """test the correct answer"""
        self.assertEqual(access_nested_map(value, path), expected)