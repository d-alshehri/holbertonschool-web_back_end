#!/usr/bin/env python3
"""
This module contains a helper function for pagination
that calculates start and end indexes for a given page.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index
        and the end index for the page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
