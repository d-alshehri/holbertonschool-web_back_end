#!/usr/bin/env python3
"""
This module contains a Server class that paginates
a database of popular baby names and provides
hypermedia-style pagination metadata.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


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
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE: str = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server with dataset cache."""
        self.__dataset: List[List[Any]] = None

    def dataset(self) -> List[List[Any]]:
        """
        Return the cached dataset loaded from the CSV file.

        Returns:
            List[List[Any]]: The dataset as a list of lists.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[Any]]:
        """
        Retrieve a page of the dataset.

        Args:
            page (int): The current page number (1-indexed), must be > 0.
            page_size (int): The number of items per page, must be > 0.

        Returns:
            List[List[Any]]: The requested page of data. Returns an empty list
            if the page is out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieve hypermedia pagination metadata.

        Args:
            page (int): The current page number (1-indexed), must be > 0.
            page_size (int): The number of items per page, must be > 0.

        Returns:
            Dict[str, Any]: A dictionary containing:
                - page_size (int): The length of the returned dataset page.
                - page (int): The current page number.
                - data (List[List[Any]]): The dataset page.
                - next_page (int or None): Number of the next page, None if no next page.
                - prev_page (int or None): Number of the previous page, None if no previous page.
                - total_pages (int): Total number of pages.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
