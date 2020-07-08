import bisect
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i, L = 0, []
        for j in range(len(nums)):
            bisect.insort(L, nums[j])
            if L[-1] - L[0] > limit:
                L.pop(bisect.bisect(L, nums[i])-1)
                i += 1
            return j - i + 1