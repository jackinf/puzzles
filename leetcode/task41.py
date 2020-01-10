from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # edge cases
        if 1 not in nums:
            return 1
        if nums == [1]:
            return 2

        # replace zeros, negatives and larger than n with 1s
        for i in range(n):
            if not (0 < nums[i] <= n):
                nums[i] = 1

        # change the signs of ath elements if present
        for num in nums:
            a = abs(num)
            if a == n:
                nums[0] = -1 * abs(nums[0])  # as the array is n elements, then use 0th element for nth element
            else:
                nums[a] = -1 * abs(nums[a])

        # get index of the first positive element
        for i in range(1, n):
            if nums[i] > 0:
                return i

        # check if the first element was not marked as negative. As the array is of length n, we reserve 0th index for n value
        if nums[0] > 0:
            return n

        # did not find any positive elements
        return n + 1


if __name__ == "__main__":
    s = Solution()
    assert(s.firstMissingPositive([1, 2]) == 3)
    assert(s.firstMissingPositive([3, 4, -1, 1]) == 2)
    assert(s.firstMissingPositive([7, 8, 9, 11, 12]) == 1)
    assert(s.firstMissingPositive([3, 4, -1, -2, 1, 5, 16, 0, 2, 0]) == 6)
    print('All tests ran successfully')
