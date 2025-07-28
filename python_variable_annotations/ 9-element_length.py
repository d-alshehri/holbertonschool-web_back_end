#!/usr/bin/env python3
"""
Module 9-element_length
Provides a function that returns the length of elements in an iterable of sequences.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence-like objects (e.g., strings, lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
