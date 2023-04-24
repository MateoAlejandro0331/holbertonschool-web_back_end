#!/usr/bin/python3
"""Define put and get method to access data"""
BasicCache = __import__('0-basic_cache').BasicCache


class FIFOCache(BasicCache):
    """Define fifo class"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            print("DISCARD: {}".format(list(self.cache_data.keys())[0]))
            del self.cache_data[list(self.cache_data.keys())[0]]

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
