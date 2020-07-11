from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = len(nums) - 2
        while p1 >= 0 and nums[p1] >= nums[p1 + 1]:
            p1 -= 1

        if p1 >= 0:
            p2 = len(nums) - 1
            while p2 > p1 and nums[p1] >= nums[p2]:
                p2 -= 1
            nums[p1], nums[p2] = nums[p2], nums[p1]

        p1 += 1
        p2 = len(nums) - 1

        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 -= 1