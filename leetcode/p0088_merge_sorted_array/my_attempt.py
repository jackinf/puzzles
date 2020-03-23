from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        p1, p2, processed = m - 1, n - 1, 0
        for i in range(m + n - 1, -1, -1):
            if p1 == -1 or nums1[p1] <= nums2[p2]:
                nums1[i], nums2[p2] = nums2[p2], nums1[i]
                p2 -= 1

                if p2 == -1:
                    break
            else:
                nums1[i], nums1[p1] = nums1[p1], nums1[i]
                p1 -= 1


if __name__ == "__main__":
    arr1 = [1, 2, 3, 0, 0, 0]
    Solution().merge(arr1, 3, [2, 5, 6], 3)
    print(arr1)