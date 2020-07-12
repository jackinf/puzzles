from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = self.binarySearch(nums, target)
        if index == -1:
            return [-1, -1]
        return self.expand(nums, index)

    def binarySearch(self, nums, target):
        p1, p2 = 0, len(nums) - 1

        while p1 <= p2:
            m = p1 + (p2 - p1) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                p1 = m + 1
            else:
                p2 = m - 1
        return -1

    def expand(self, nums, index):
        ans = [index, index]

        for i in range(index + 1, len(nums)):
            if nums[i] != nums[index]:
                break
            ans[1] = i

        for i in range(index - 1, -1, -1):
            if nums[i] != nums[index]:
                break
            ans[0] = i

        return ans