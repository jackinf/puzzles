from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        answer = [0] * N
        answer[0] = 1
        for i in range(1, N):
            answer[i] = nums[i-1] * answer[i-1]

        R = 1
        for i in reversed(range(N)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer


if __name__ == "__main__":
    s = Solution()

    arr = [1, 2, 3, 4]
    print(s.productExceptSelf(arr))  # [24, 12, 8, 6]