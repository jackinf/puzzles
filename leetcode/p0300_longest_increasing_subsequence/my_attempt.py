from collections import defaultdict
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cc = defaultdict(list)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    cc[i].append(j)

        q = []
        for i in range(len(nums) - 1, -1, -1):
            q.append((i, 1))

        res = 1
        while q:
            curr, d = q.pop(0)
            res = max(res, d)
            for j in cc[curr]:
                q.append((j, d + 1))

        return res