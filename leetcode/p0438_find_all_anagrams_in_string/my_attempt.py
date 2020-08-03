from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []

        p_counter = Counter(p)
        window = Counter(s[:len(p)])

        res = []
        if window == p_counter:
            res.append(0)

        for i in range(len(p), len(s)):
            p1, p2 = s[i - len(p)], s[i]
            window[p2] += 1
            window[p1] -= 1
            if window[p1] == 0:
                del window[p1]

            if window == p_counter:
                res.append(i - len(p) + 1)

        return res