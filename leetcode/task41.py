from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pass


"""
10 2 1 20 9

1 10 2
"""

sol = Solution()
assert(sol.firstMissingPositive([1, 2, 0]) == 3)
assert(sol.firstMissingPositive([3, 4, -1, 1]) == 2)
assert(sol.firstMissingPositive([7, 8, 9, 11, 12]) == 1)
