#!/usr/bin/env python3


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
            assert isinstance(page, int) and page > 0
            assert isinstance(page_size, int) and page_size > 0
            
            total_size = len(self.dataset())
            total_pages = (total_size + page_size - 1) // page_size
            
            if (page > total_pages and page_size > total_size):
                return []
            
            index_range(page, page_size)