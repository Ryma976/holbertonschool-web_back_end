#!/usr/bin/env python3
"""Module for task 10: Duck typing - first element of a sequence."""
from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of a sequence if it exists, otherwise None."""
    if lst:
        return lst[0]
    else:
        return None
