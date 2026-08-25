#!/usr/bin/env python3
"""Module for task 6: Complex types - mixed list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate and return the sum of a list of integers and floats as a float."""
    return float(sum(mxd_lst))
