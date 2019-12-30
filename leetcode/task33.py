from typing import List


class Solution:
    def search_v1(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        diff = mid_i = int(len(nums) / 2)
        crossed_pivot = False
        prev_mid_i = 0

        while abs(mid_i - prev_mid_i) != 0:
            mid = nums[mid_i]
            if mid == target:
                return mid_i
            if crossed_pivot is False:
                crossed_pivot = nums[prev_mid_i] > nums[mid_i]
            left_index = mid_i if crossed_pivot is True else 0
            diff = int(diff / 2) if nums[left_index] > target else -int(diff / 2)
            diff *= -1 if crossed_pivot else 1
            prev_mid_i = mid_i
            mid_i += diff

        return -1


    def search(self, nums: List[int], target: int) -> int:
        def sol(i, j):
            if i > j:
                return -1
            if i == j and nums[i] != target:
                return -1
            m = int((i + j) / 2)
            if nums[m] == target:
                return m
            if nums[m + 1] <= nums[j]:  # second half is in sorted order
                if nums[m + 1] <= target <= nums[j]:  # target lies in the range of second order
                    return sol(m + 1, j)
                else:
                    return sol(i, m - 1)
            else:  # first half is in sorted order
                if nums[i] <= target <= nums[m - 1]:  # target ies in the range of first half
                    return sol(i, m - 1)
                else:
                    return sol(m + 1, j)

        return sol(0, len(nums) - 1)


s = Solution()
# print(s.search([1, 2], 1))
# print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
# print(s.search([4, 5, 6, 7, 0, 1, 2], 6))
print(s.search([4, 5, 6, 7, 8, 1, 2], 8))
