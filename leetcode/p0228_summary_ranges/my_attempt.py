from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        start, prev = nums[0], nums[0]
        res = []
        nums.append(float('inf'))
        for i in range(len(nums)):
            num, prev = nums[i], nums[i-1]
            if num - prev > 1:
                res.append(str(start) if start == prev else f"{start}->{prev}")
                start = num
        return res