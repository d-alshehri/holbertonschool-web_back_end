#!/usr/bin/env python3
"""
Module 7-to_kv
Provides a function that returns a tuple with a string
and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of a number as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): A number to be squared.

    Returns:
        Tuple[str, float]:
        A tuple with the original string and the square of v.
    """
    return (k, float(v ** 2))
