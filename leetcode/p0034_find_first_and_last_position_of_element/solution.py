class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo, high = 0, len(nums)-1

        # [5,7,7,8,8,10]
        while lo < high:
            mid = lo+(high-lo)//2

            if nums[mid] > target or (left and nums[mid] == target):
                high = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        ind = self.extreme_insertion_index(nums, target, True)
        if ind == len(nums) or nums[ind] != target:
            return [-1, -1]
        return [ind, self.extreme_insertion_index(nums, target, False)-1]


if __name__ == "__main__":
    print(Solution().searchRange([5,7,7,8,8,10], 8))