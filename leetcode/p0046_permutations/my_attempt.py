from typing import List


class Solution:
    """
    Accepted
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.LL = []
        self.solve(nums, [])
        return self.LL

    def solve(self, nums: List[int], res: List[int]):
        if len(nums) == 0:
            return
        if len(nums) == 1:
            res.append(nums[0])
            self.LL.append(res)
            return

        for i in range(len(nums)):
            self.solve(nums[:i] + nums[i + 1:], res + [nums[i]])