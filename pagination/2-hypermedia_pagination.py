#!/usr/bin/env python3
"""Implement a method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10."""
import csv
import math
from typing import Dict, List


def index_range(page, page_size):
    """Returns a tuple"""
    start_index = (page - 1) * page_size
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
        """Method to call index_range"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        self.dataset()
        index = index_range(page, page_size)
        return self.__dataset[index[0]: index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Method that call get_page"""
        data = self.get_page(page, page_size)
        total_data = self.dataset()
        total_pages = len(total_data) // page_size
        next_page = page + 1
        if next_page > total_pages:
            next_page = None
        prev_page = page - 1
        if prev_page < 1:
            prev_page = None
        
        return {
                'page_size': page_size, 
                'page': page, 
                'data': data, 
                'next_page': next_page, 
                'prev_page': prev_page, 
                'total_pages': total_pages
                }
