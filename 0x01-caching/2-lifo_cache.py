#!/usr/bin/env python3
""" LIFO cache
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching class"""
    
    def __init__(self):
        """ Initializing
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """place the key and item using lifo method"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            last_key = [keys[-1]]
            print(last_key)
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """get the value of the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]