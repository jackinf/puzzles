from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sums = [0] * len(nums)
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = nums[i] + sums[i - 1]

        min_sum, res = 0, max(nums)
        for i in range(len(sums)):
            if sums[i] > min_sum:
                res = max(sums[i] - min_sum, res)
            else:
                min_sum = min(min_sum, sums[i])

        return res


if __name__ == "__main__":
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))