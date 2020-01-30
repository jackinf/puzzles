from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        def solve(i: int, sum: int) -> int:
            i_plus_one_sum = sum if i + 2 >= len(nums) else solve(i + 2, sum + nums[i + 2])
            i_plus_two_sum = sum if i + 3 >= len(nums) else solve(i + 3, sum + nums[i + 3])

            return max(i_plus_one_sum, i_plus_two_sum)

        return solve(-2, 0)


if __name__ == "__main__":
    s = Solution()

    print(s.rob([1,2,3,1]))
    print(s.rob([2,7,9,3,1]))
    print(s.rob([155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165]))