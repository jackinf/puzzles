from typing import List, Set, Dict
from collections import defaultdict, Counter


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        m = defaultdict(set)
        degrees = {k:0 for k in set([x for y in words for x in y])}
        if not words:
            return ""

        for i in range(len(words)-1):
            curr = words[i]
            nexx = words[i+1]
            shorter = min(len(curr), len(nexx))
            for j in range(shorter):
                c1 = curr[j]
                c2 = nexx[j]
                if c1 != c2:
                    if c1 not in m:
                        m[c1] = set()
                    if c2 not in m[c1]:
                        m[c1].add(c2)
                        degrees[c2] += 1
                    break

        q = []
        for i in degrees:
            if degrees[i] == 0:
                q.append(i)

        res = ""
        while q:
            c1 = q.pop(0)
            res += c1
            for c2 in m[c1]:
                degrees[c2] -= 1
                if degrees[c2] == 0:
                    q.append(c2)

        if len(res) != len(degrees):
            return ""

        return res


if __name__ == "__main__":
    s = Solution()

    inp01 = ["wrt", "wrf", "er", "ett", "rftt"]
    print(s.alienOrder(inp01))