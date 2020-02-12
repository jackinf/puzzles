from collections import defaultdict
from typing import List


class Solution:
    """
    Invalid
    """
    def alienOrder(self, words: List[str]) -> str:
        p1, p2, max_p2 = 0, 0, 0
        res = defaultdict(list)
        while p1 < len(words):
            curr = words[p1]
            if p1 > 0:
                prev = words[p1 - 1]
                if p2 < len(prev) and p2 < len(curr) and curr[p2] == prev[p2]:
                    p2 += 1
                    if len(curr) < p2 <= len(prev) - 1:
                        return ""
                    continue

            if p2 >= len(words[p1]):
                p1 += 1
                p2 = 0
                continue
            letter = words[p1][p2]
            res[p2].append(letter)
            max_p2 = max(max_p2, p2)
            p1 += 1
            p2 = 0

        res1_s = ""
        for i in range(max_p2 + 1):
            for items in res[i]:
                for x in items:
                    res1_s += x
        if len(set(res1_s)) != len(res1_s):
            return ""
        return res1_s
