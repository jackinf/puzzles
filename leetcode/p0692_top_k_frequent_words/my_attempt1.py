from collections import Counter, defaultdict
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        dict1 = defaultdict(list)

        for key, v in counter.items():
            heapq.heappush(dict1[v], key)

        res, analyzed = [], 0
        for key in sorted(dict1.keys(), reverse=True):
            while dict1[key]:
                res.append(heapq.heappop(dict1[key]))
                analyzed += 1
                if analyzed == k:
                    return res

        return res