#!/usr/bin/env python3
"""
This script defines a type-annotated function sum_list
to calculate the sum of a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.
    """
    return sum(input_list)
