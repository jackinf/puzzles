from typing import List


class Solution:
    """
    Great speed :)
    """
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0

        maxres1 = float('-inf')
        res1 = 1
        for i in range(len(nums)):
            res1 *= nums[i]
            maxres1 = max(res1, maxres1)
            res1 = res1 if res1 != 0 else 1

        maxres2 = float('-inf')
        res2 = 1
        for i in range(len(nums) - 1, 0, -1):
            res2 *= nums[i]
            maxres2 = max(res2, maxres2)
            res2 = res2 if res2 != 0 else 1

        return max(maxres1, maxres2)