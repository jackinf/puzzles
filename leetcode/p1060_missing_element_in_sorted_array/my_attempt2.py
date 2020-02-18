from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        diffs = [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            diffs[i - 1] = nums[i] - nums[i - 1] - 1

        for i, diff in enumerate(diffs):
            if k > diff:
                k -= diff
                continue
            return nums[i] + k

        return nums[-1] + k