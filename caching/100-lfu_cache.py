#!/usr/bin/python3
"""Define put and get method to access data"""
BasicCache = __import__('0-basic_cache').BasicCache


class LFUCache(BasicCache):
    """Define LFUCache"""

    def __init__(self):
        super().__init__()
        self.freq_keys = []

    def put(self, key, item):
        """Put an item"""
        if key is None or item is None:
            return

        if key in self.freq_keys:
            self.freq_keys.remove(key)

        elif len(self.freq_keys) >= self.MAX_ITEMS:
            last_key = self.freq_keys.pop(0)
            print("DISCARD: {}".format(last_key))
            del self.cache_data[last_key]
        self.freq_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        self.freq_keys.remove(key)
        self.freq_keys.append(key)
        return self.cache_data[key]
