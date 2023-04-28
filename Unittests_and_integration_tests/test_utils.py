#!/usr/bin/env python3
"""Creating unittests"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, value, path) -> Any:
        """ Test the access nested map exceptions """
        with self.assertRaises(KeyError):
            access_nested_map(value, path)


class TestGetJson(unittest.TestCase):
    """Test Get JSON"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock) -> Any:
        """ Test the method"""
        mock.return_value = test_payload
        response = get_json(test_url)
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """ Test Memoize class"""

    def test_memoize(self):
        """ Test Memoize"""
        class TestClass:
            """Test Class"""
            def a_method(self):
                """Just a method"""
                return 42

            @memoize
            def a_property(self):
                """Just a property"""
                return self.a_method()

        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once
