from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cache = {0: -1}
        res = 0
        for i in range(len(nums)):
            res += nums[i]

            if k != 0:
                res %= k

            if res in cache:
                if i - cache[res] > 1:
                    return True
            else:
                cache[res] = i

        return False


if __name__ == "__main__":
    arr = [23, 2, 6, 4, 7]
    k = 6
    print(Solution().checkSubarraySum(arr, k))