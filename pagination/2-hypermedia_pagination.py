#!/usr/bin/env python3
"""This module provides tools for paginating a CSV dataset of baby names."""
import csv
from typing import List, Tuple, Dict, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a specific pagination request.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names from a CSV file."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with no dataset loaded."""
        self.__dataset: Optional[List[List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """
        Load and cache the dataset from the CSV file.

        Returns:
            list: A list of rows, where each row is a list of strings.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Retrieve a specific page of the dataset.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            list: A list of rows for the requested page.
        """
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Optional[object]]:
        """
        Return hypermedia pagination details for the dataset.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            dict: A dictionary containing pagination information and data.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = (total_items + page_size - 1) // page_size  # Ceiling division

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
