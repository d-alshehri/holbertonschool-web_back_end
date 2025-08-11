#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination module.
Provides the Server class which supports indexed pagination
that is robust to deletions in the dataset.
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server with dataset and indexed dataset cache."""
        self.__dataset: List[List[Any]] = None
        self.__indexed_dataset: Dict[int, List[Any]] = None

    def dataset(self) -> List[List[Any]]:
        """
        Return the cached dataset.
        Loads the dataset from CSV if it has not been loaded yet.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[Any]]:
        """
        Return the dataset indexed by position starting at 0.
        This index allows for deletion-resilient pagination.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary for deletion-resilient pagination.

        Args:
            index: The start index of the page (0-based).
            page_size: The number of items per page.

        Returns:
            A dictionary containing:
                - index: The start index of the current page
                - next_index: The start index of the next page
                - page_size: The number of items in the current page
                - data: The actual page of data
        """
        indexed_data = self.indexed_dataset()
        assert index is not None and 0 <= index < len(indexed_data)

        data: List[List[Any]] = []
        current_index = index

        while len(data) < page_size and current_index < len(indexed_data):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        next_index = current_index if current_index < len(indexed_data) else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
