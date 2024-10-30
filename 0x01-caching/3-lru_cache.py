#!/usr/bin/python3
""" BasicCache module using the FIFO policy.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Stores and retirevies an item from cache
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.hits_count = {}

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and move it to the end
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Pop the first (oldest) item
                lru_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end (most recently used)
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
