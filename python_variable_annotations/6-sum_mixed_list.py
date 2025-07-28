#!/usr/bin/env python3
"""
Module 6-sum_mixed_list
Provides a function that sums a list containing integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats as a float.

    Args:
        mxd_lst (List[Union[int, float]]):
        A list containing integers and floats.

    Returns:
        float: The sum of the values in the list.
    """
    return sum(mxd_lst)
