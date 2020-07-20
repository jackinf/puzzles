from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        self.recurse(nums, results, set())
        return results

    def recurse(self, nums, results, seen):
        numstuple = tuple(nums)
        if numstuple in seen:
            return
        seen.add(numstuple)

        if not nums:
            return

        results.append(nums)
        for i in range(len(nums)):
            self.recurse(nums[:i] + nums[i + 1:], results, seen)