#!/usr/bin/env python3
"""
This script defines a type-annotated function
make_multiplier to create a function
that multiplies a float by a given multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a function that multiplies a float by a given multiplier."""
    def multiply(num: float) -> float:
        return num * multiplier
    return multiply
