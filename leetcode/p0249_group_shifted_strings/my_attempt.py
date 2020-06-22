from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        cache = defaultdict(list)

        for s1 in strings:
            start = ord(s1[0]) - 1
            key = tuple(((ord(x) - start) % 26 for x in s1))
            cache[key].append(s1)

        return list(cache.values())