from typing import List


class Solution:
    def nextPermutation_v3(self, nums: List[int]) -> None:
        num = 0
        index = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] < nums[i]:
                num = nums[i-1]
                index = i-1
                break

        if index is None:
            nums.reverse()
            return

        for i in range(index+1, len(nums)):
            if nums[i] < num:
                nums[i-1], nums[index] = nums[index], nums[i-1]
                nums[index + 1:] = reversed(nums[index + 1:])
                return

        # prev = float('inf')
        # p_index = -1
        #
        # for i in range(index + 1, len(nums)):
        #     if num < nums[i] <= prev:
        #         prev = nums[i]
        #         p_index = i
        #
        # nums[index], nums[p_index] = nums[p_index], nums[index]
        # nums[index + 1:] = reversed(nums[index + 1:])


    # def nextPermutation_v2(self, nums: List[int]) -> None:
    #     i = 0
    #     x = None  # smallest on left
    #     y = None  # next smallest
    #     decreasing = True
    #
    #     while i < len(nums)-1:
    #         i += 1
    #         if nums[i-1] > nums[i]:
    #             decreasing = True
    #             if x is not None:
    #                 y = i
    #         elif nums[i-1] < nums[i]:
    #             x = i-1
    #             decreasing = False
    #             if y is not None:
    #                 break
    #
    #     if decreasing is False and x is not None:
    #         nums[x], nums[x+1] = nums[x+1], nums[x]
    #     if decreasing is True and x is not None:
    #         nums[x + 1:] = reversed(nums[x + 1:])




    # def nextPermutation_v1(self, nums: List[int]) -> None:
    #     i = len(nums)
    #     swap_index = None
    #     move_right = False
    #     while True:
    #         if move_right is False:
    #             i -= 1
    #             if i <= 0:
    #                 nums.sort()
    #                 return
    #             if nums[i - 1] < nums[i]:
    #                 if swap_index is None:
    #                     continue
    #                 nums[swap_index], nums[i-1] = nums[swap_index], nums[i-1]
    #                 move_right = True
    #                 continue
    #             elif nums[i - 1] == nums[i]:
    #                 continue
    #             else:
    #                 swap_index = i
    #
    #         if move_right is True:
    #             i += 1
    #             if i >= len(nums):
    #                 return
    #             if nums[i - 1] > nums[i]:
    #                 nums[i], nums[i-1] = nums[i-1], nums[i]
    #                 continue
    #             else:
    #                 return


s = Solution()
all = []
# all.append([1, 2, 3])
all.append([1, 3, 2])
# all.append([1, 5, 8, 4, 7, 6, 5, 3, 1])
# all.append([3, 2, 1])
# all.append([1, 1, 5])
for item in all:
    s.nextPermutation_v3(item)
    print(item)
