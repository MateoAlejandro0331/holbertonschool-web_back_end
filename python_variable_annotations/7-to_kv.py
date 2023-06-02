#!/usr/bin/env python3
"""
This script defines a type-annotated function
to_kv to create a tuple with a string and the
square of an int or float.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with a string and the square of an int or float.
    """
    return k, float(v ** 2)
