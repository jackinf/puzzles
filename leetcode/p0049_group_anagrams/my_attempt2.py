from typing import List


class Solution:
    """
    Accepted, good speed
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        levels = []

        for s in strs:
            key = ''.join(sorted(s))
            if key not in seen:
                seen[key] = len(levels)
                levels.append([])
            levels[seen[key]].append(s)

        return levels