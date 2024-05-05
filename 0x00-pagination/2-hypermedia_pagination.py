#!/usr/bin/env python3
"""a module for simple pagination"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> int:
    """
    Args:
    - page: page to to be retrieved
    -page_size: size of the page
    
    Returns a tuple of size two containing a start index and an end index
    """
    start_index = (page - 1)* page_size
    end_index = start_index + page_size
    return (start_index, end_index)



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
        """returns appropriate page of the csv"""
        assert isinstance(page, int)
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        total_size = len(self.dataset())
        total_pages = (total_size + page_size - 1) // page_size

        if (page > total_pages and page_size > total_size):
            return []

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns data  from dataset with hypermedia"""
        data = self.dataset()
        total_pages = (len(data) + page_size - 1) // page_size
        retrieved_data_set = self.get_page(page, page_size)
        return {
         'page_size': page_size,
         'page': page,
         'data': retrieved_data_set,
         'next_page': f"{min(page + 1, total_pages)}" if page < total_pages else None,
         'prev_page': f"{max(page - 1, 1)}" if page > 1 else None,
         'total_pages': total_pages
        }
