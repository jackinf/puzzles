from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.solution2(nums)

    def solution2(self, nums: List[int]) -> List[int]:
        N = len(nums)
        cache = [1] * N
        for i in range(N-1):
            nums.append(nums.pop(0))
            cache[i] *= nums[i]

    def brute_force(self, nums: List[int]) -> List[int]:
        N = len(nums)
        cache = [1] * N

        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                cache[i] *= nums[j]

        print(cache)
        return cache



if __name__ == "__main__":
    s = Solution()

    arr = [1, 2, 3, 4]
    print(s.productExceptSelf(arr))  # [24, 12, 8, 6]