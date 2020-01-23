from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        L, R, C = [0]*N, [0]*N, [0]*N

        L[0] = 1
        for i in range(1, N):
            L[i] = nums[i-1] * L[i-1]
        print(L)

        R[N-1] = 1
        for i in reversed(range(N-1)):
            R[i] = nums[i+1] * R[i+1]
        print(R)

        for i in range(N):
            C[i] = L[i]*R[i]

        return C

if __name__ == "__main__":
    s = Solution()

    arr = [1, 2, 3, 4]
    print(s.productExceptSelf(arr))  # [24, 12, 8, 6]