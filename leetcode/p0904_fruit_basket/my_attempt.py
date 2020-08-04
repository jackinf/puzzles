from collections import Counter
from typing import List


class Solution:
    """ Accepted """
    def totalFruit(self, tree: List[int]) -> int:
        p1 = p2 = max_res = 0
        counter, t = Counter(), 0

        while p1 < len(tree) and p2 < len(tree):
            if t <= 2:
                if counter[tree[p2]] == 0:
                    t += 1
                counter[tree[p2]] += 1
                p2 += 1

                if t <= 2 and max_res < p2 - p1:
                    max_res = p2 - p1
            else:
                counter[tree[p1]] -= 1
                if counter[tree[p1]] == 0:
                    t -= 1
                p1 += 1

        return max_res