#!/usr/bin/python3
"""Define put and get method to access data"""
BasicCache = __import__('0-basic_cache').BasicCache


class LIFOCache(BasicCache):
    """Define LIFOCache"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put an item"""
        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            self.cache_data.pop(key)

        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-2]
            print("DISCARD: {}".format(last_key))
            del self.cache_data[last_key]

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
