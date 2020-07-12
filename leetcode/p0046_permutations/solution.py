from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)

        def backtrack(first = 0):
            if first == n:
                output.append(nums[:])
            else:
                for i in range(first, n):
                    nums[i], nums[first] = nums[first], nums[i]
                    backtrack(first + 1)
                    nums[i], nums[first] = nums[first], nums[i]

        backtrack()
        return output


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))