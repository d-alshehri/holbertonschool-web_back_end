#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.

This module defines a Server class that can paginate a dataset
while handling the case where rows are removed between requests,
ensuring that the user does not miss any items when changing pages.
"""

import csv
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server without loading the dataset."""
        self.__dataset: Optional[List[List[str]]] = None
        self.__indexed_dataset: Optional[Dict[int, List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """
        Load and cache the dataset from the CSV file.

        Returns:
            list: A list of rows from the dataset (each row is a list of strings).
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """
        Create and cache an indexed version of the dataset.

        The keys are the original positions of the rows in the dataset.
        This allows deletion-resilient pagination.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient paginated page.

        Args:
            index (int): The current start index for the page.
            page_size (int): The number of items to include in the page.

        Returns:
            dict: A dictionary containing:
                - index: The current start index of the return page.
                - next_index: The index to query next.
                - page_size: The current page size.
                - data: The actual page of the dataset.

        Raises:
            AssertionError: If index is out of range.
        """
        indexed_data = self.indexed_dataset()
        data_length = len(indexed_data)

        assert index is not None and 0 <= index < data_length, \
            "Index is out of range"

        data: List[List[str]] = []
        current_index = index

        # Collect exactly `page_size` items, skipping missing indexes
        while len(data) < page_size and current_index < max(indexed_data.keys()) + 1:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        next_index = current_index

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
