from collections import defaultdict


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = [0]*300
        self.hits = [0]*300

    def hit(self, timestamp: int) -> None:
        index = timestamp % 300
        if self.times[index] != timestamp:
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        return total