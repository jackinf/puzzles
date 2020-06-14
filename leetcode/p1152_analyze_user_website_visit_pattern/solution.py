from collections import defaultdict, Counter
from itertools import combinations
from typing import List


class Solution:
    def mostVisitedPattern(self, usernames: List[str], timestamps: List[int], websites: List[str]) -> List[str]:
        N = len(usernames)

        # step 1: add website per user, sorted by timestamp
        mapping = defaultdict(list)
        for t, u, w in sorted(zip(timestamps, usernames, websites)):
            mapping[u].append(w)

        # step 2: add all combinations into counter
        cnt = Counter()
        for website_list in mapping.values():
            comb = set(combinations(website_list, 3))
            for item in comb:
                cnt[item] += 1

        # step 3 sort by occurrences, then by letters
        result = sorted(cnt, key=lambda x: (-cnt[x], x))[0]
        return result