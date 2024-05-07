#!/usr/bin/env python3
"""This is a simple pagination"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """A function to calcualt ethe start and end of a page"""
    start: int = (page - 1) * page_size
    end: int = page * page_size
    return start, end


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
        """Returns sthe appropriate page of the dataser"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return the dictionary of paginaition resuls"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": page + 1 if page + 1 <= total_pages else None,
                "prev_page": page - 1 if page - 1 > 0 else None,
                "total_pages": total_pages,
                }