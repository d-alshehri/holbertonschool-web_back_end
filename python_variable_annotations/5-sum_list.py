#!/usr/bin/env python3
"""
Module 5-sum_list
Provides a function to sum a list of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of float numbers.

    Args:
        input_list (List[float]): A list of float numbers to be summed.

    Returns:
        float: The total sum of the list.
    """
    return sum(input_list)
