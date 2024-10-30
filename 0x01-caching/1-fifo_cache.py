#!/usr/bin/python3
""" BasicCache module using the FIFO policy.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Stores and retirevies an item from cache
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds items to the cache,
        removes the first inserted item
        if the items more than the max_items"""
        if key is None or item is None:
            return
        if len(self.cache_data) < self.MAX_ITEMS:
            self.cache_data[key] = item
        else:
            first_item, _ = self.cache_data.popitem(last=False)
            self.cache_data[key] = item
            print(f"DISCARD: {first_item}")

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
