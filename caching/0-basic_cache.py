#!/usr/bin/python3
"""Define put and get method to access data"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Define basic caching"""
    
    def __init__(self):
        super().__init__()
