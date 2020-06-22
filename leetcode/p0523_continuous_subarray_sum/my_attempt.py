from typing import List


class Solution:
    """
    O(n^2) bruteforce, very slow but accepted
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dp = nums[:]
        for length in range(2, len(nums) + 1):
            for i in range(len(nums) - length + 1):
                res = dp[i] + nums[i + length - 1]
                dp[i] = res
                if (k == 0 and res == 0) or k != 0 and res % k == 0:
                    return True

        return False