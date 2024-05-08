#!/usr/bin/env python3
""" least frequently used algorithm
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """lfu caching class"""

    def __init__(self):
        super().__init__()
        self.lfu = {}

    def put(self, key, item):
        """place items in cache using lfu"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.lfu:
                self.lfu[key] += 1
            else:
                self.lfu[key] = 1
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_frequent_key = min(self.lfu, key=self.lfu.get)
                del self.cache_data[least_frequent_key]
                del self.lfu[least_frequent_key]
                print("DISCARD: {}".format(least_frequent_key))

    def get(self, key):
        """getter function"""
        if key is not None or key in self.cache_data:
            if key in self.cache_data:
                self.lfu[key] += 1
                return self.cache_data[key]
