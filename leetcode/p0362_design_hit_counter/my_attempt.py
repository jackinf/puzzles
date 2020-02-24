from collections import defaultdict


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = defaultdict(int)
        self.hits = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.cache[timestamp] += 1
        self.resize(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.resize(timestamp)
        return self.hits

    def resize(self, timestamp: int) -> int:
        self.hits = 0
        start, end = max(0, timestamp - 299), timestamp + 1
        new_cache = defaultdict(int)
        for i in range(start, end):
            new_cache[i] = self.cache[i]
            self.hits += new_cache[i]
        self.cache = new_cache