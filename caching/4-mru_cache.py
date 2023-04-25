#!/usr/bin/python3
"""Define put and get method to access data"""
BasicCache = __import__('0-basic_cache').BasicCache


class MRUCache(BasicCache):
    """Define LRUCache"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put an item"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= self.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(last_key))
            del self.cache_data[last_key]
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
