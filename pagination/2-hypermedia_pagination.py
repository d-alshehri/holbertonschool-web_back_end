#!/usr/bin/env python3
"""Provides a function index_range"""
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size) -> tuple:
    """Returns pagination params into a list of data"""
    limit = page * page_size
    offset = (page - 1) * page_size
    return (offset, limit)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Returns a paginated data set according to params"""
        assert (type(page) == int and page > 0)
        assert (type(page_size) == int and page_size > 0)
        offset, end = index_range(page, page_size)
        return self.dataset()[offset:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a hypermedia data for api purpose"""
        data_count = len(self.dataset())
        hyper_data = {}
        hyper_data["page_size"] = page_size
        hyper_data["page"] = page
        hyper_data["data"] = self.get_page(page, page_size)
        next_offset, next_limit = index_range(page + 1, page_size)
        try:
            self.dataset()[next_offset]
            hyper_data["next_page"] = page + 1
        except IndexError:
            hyper_data["next_page"] = None
        if page > 2:
            hyper_data["prev_page"] = page - 1
        else:
            hyper_data["prev_page"] = None
        hyper_data["total_pages"] = int(data_count/page_size) + 1
        return hyper_data