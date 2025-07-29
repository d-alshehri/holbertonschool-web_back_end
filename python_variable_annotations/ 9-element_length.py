#!/usr/bin/env python3
"""Annotate the below function’s parameters and
return values with the appropriate types"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples, each tuple containing an element"""
    return [(i, len(i)) for i in lst]
