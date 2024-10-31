#!/usr/bin/python3
"""A class that sets, gets items from a data dictionary,
using the LFU algorithm with LRU tie-breaking"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """A class that sets and gets items based on the LFU algorithm,
       with LRU tie-breaking for items with the same frequency."""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.hit_counts = {}

    def put(self, key, item):
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.hit_counts[key] += 1
        else:
            # Check if cache is full
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_frequency = min(self.hit_counts.values())
                min_keys = [k for k, v in self.hit_counts.items()
                            if v == min_frequency]

                if len(min_keys) > 1:
                    min_key = next(k for k in self.cache_data if k in min_keys)
                else:
                    min_key = min_keys[0]

                del self.cache_data[min_key]
                del self.hit_counts[min_key]
                print(f"DISCARD: {min_key}")

            # Add the new item with a hit count of 1
            self.cache_data[key] = item
            self.hit_counts[key] = 1

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        self.hit_counts[key] += 1
        self.cache_data.move_to_end(key)

        return self.cache_data[key]
