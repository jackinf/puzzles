from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k < 1 or not s:
            return 0

        maxlength, size, p1, p2 = 0, 0, -1, -1
        window = Counter()

        while p1 < len(s) and p2 < len(s):
            if size <= k:
                p2 += 1
                if p2 == len(s):
                    return maxlength
                window[s[p2]] += 1
                if window[s[p2]] == 1:
                    size += 1
            else:
                p1 += 1
                if p1 == len(s):
                    return maxlength
                window[s[p1]] -= 1
                if window[s[p1]] == 0:
                    size -= 1

            if size <= k:
                maxlength = max(maxlength, p2 - p1)
        return maxlength