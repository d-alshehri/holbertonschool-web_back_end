#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination module.

This module provides the Server class which paginates
a dataset of popular baby names indexed by position,
allowing pagination that is resilient to deletions.
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE: str = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize Server with dataset and indexed dataset cache."""
        self.__dataset: List[List[Any]] = None
        self.__indexed_dataset: Dict[int, List[Any]] = None

    def dataset(self) -> List[List[Any]]:
        """
        Load and cache the dataset from the CSV file.

        Returns:
            List[List[Any]]: The dataset as a list of rows.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header row
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[Any]]:
        """
        Create and cache a dict indexed dataset where keys are
        the original indices, supporting deletion-resilient pagination.

        Returns:
            Dict[int, List[Any]]: Indexed dataset mapping index to row.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0,
                        page_size: int = 10) -> Dict[str, Any]:
        """
        Return a deletion-resilient hypermedia pagination dictionary.

        Args:
            index (int): The starting index of the page (0-based).
            page_size (int): The number of items on the page.

        Returns:
            Dict[str, Any]: Dictionary containing:
                - index (int): The current start index.
                - next_index (int): The index to query for the next page.
                - page_size (int): The number of items on this page.
                - data (List[List[Any]]): The page of data.
        """
        indexed_data = self.indexed_dataset()
        assert isinstance(index, int) and 0 <= index < len(indexed_data)

        data: List[List[Any]] = []
        current_index = index
        collected = 0
        max_index = max(indexed_data.keys())

        while collected < page_size and current_index <= max_index:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                collected += 1
            current_index += 1

        next_index = current_index if current_index <= max_index else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
