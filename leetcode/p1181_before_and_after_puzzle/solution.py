import collections
from typing import List


class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        first = collections.defaultdict(set)
        last = collections.defaultdict(set)
        res = set()
        for p in phrases:
            strs = p.split(' ')
            if strs[0] in last:
                res1 = {a + p[len(strs[0]):] for a in last[strs[0]]}
                print('if 1', res, '++', res1)
                res |= res1
            if strs[-1] in first:
                res2 = {p + b for b in first[strs[-1]]}
                print('if 2', res, '++', res2)
                res |= res2
            first[strs[0]].add(p[len(strs[0]):])
            last[strs[-1]].add(p)
            print('first: ', first)
            print('last: ', last)
            print('====')
        return sorted(list(res))


if __name__ == "__main__":
    s = Solution()
    phrases = [
        "mission statement",
        "a quick bite to eat",
        "a chip off the old block",
        "chocolate bar",
        "mission impossible",
        "a man on a mission",
        "block party",
        "eat my words",
        "bar of soap"]
    print(s.beforeAndAfterPuzzles(phrases))