from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_map = Counter(p)
        s_map = Counter()

        res = []

        for i in range(ns):
            s_map[s[i]] += 1

            if i >= np:
                prev = s[i - np]
                if s_map[prev] == 1:
                    del s_map[prev]
                else:
                    s_map[prev] -= 1

            if p_map == s_map:
                res.append(i - np + 1)

        return res