from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        p, min_res, curr_sum = 0, float('inf'), 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            while curr_sum >= s:
                min_res = min(min_res, i-p+1)
                curr_sum -= nums[p]
                p += 1
        return 0 if min_res == float('inf') else min_res


if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))