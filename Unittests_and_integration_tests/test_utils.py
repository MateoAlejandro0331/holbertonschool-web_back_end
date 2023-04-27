#!/usr/bin/env python3
"""Creating unittests"""
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Testing access nested maps"""

    @parameterized.expand([  # Creatinf cases to pass to the method
        (2, 3, 5),
        (1, 1, 2),
        (0, 0, 0),
        (-1, 1, 0),
    ])
    def test_access_nested_map(self, ):
