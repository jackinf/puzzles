from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        anchor = 0
        for i in range(len(nums)):
            if nums[anchor] < nums[i]:
                anchor += 1
                nums[anchor] = nums[i]
        return anchor+1