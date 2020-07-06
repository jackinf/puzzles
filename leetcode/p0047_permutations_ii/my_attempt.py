from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.run(0, nums, [], res)
        return list(set(res))

    def run(self, depth, nums, acc, res):
        for i in range(len(nums)):
            if nums[i] is None:
                continue

            if depth == len(nums) - 1:
                res.append(tuple(acc + [nums[i]]))
            else:
                temp = nums[i]
                nums[i] = None
                self.run(depth + 1, nums, acc + [temp], res)
                nums[i] = temp