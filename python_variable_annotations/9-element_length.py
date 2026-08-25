#!/usr/bin/env python3
"""Module for task 9: Let's duck type an iterable object."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing each element and its length."""
    return [(i, len(i)) for i in lst]
