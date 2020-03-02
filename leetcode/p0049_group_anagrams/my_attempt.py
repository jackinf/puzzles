from collections import defaultdict, Counter
from typing import List


class Solution:
    """
    Accepted, but very slow
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = {x: Counter(x) for x in strs}
        seen = set()
        levels = []

        for i in range(len(strs)):
            if i in seen:
                continue
            levels.append([strs[i]])
            seen.add(i)

            for j in range(i + 1, len(strs)):
                if j not in seen and counters[strs[i]] == counters[strs[j]]:
                    seen.add(j)
                    levels[-1].append(strs[j])

        return levels
