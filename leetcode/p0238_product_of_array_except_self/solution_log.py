from typing import List
import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        product = 1
        for num in nums:
            product *= num

        total_log = math.log(product)
        answer = [0]* N
        for i in range(N):
            answer[i] = round(math.exp(total_log - math.log(nums[i])))

        return answer

if __name__ == "__main__":
    s = Solution()

    arr = [1, 2, 3, 4]
    print(s.productExceptSelf(arr))  # [24, 12, 8, 6]