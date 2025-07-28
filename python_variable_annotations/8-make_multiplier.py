#!/usr/bin/env python3
"""
Module 8-make_multiplier
Provides a function that creates multiplier functions using closures.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a predefined multiplier.

    Args:
        multiplier (float): The value to multiply other floats by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the product.
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
