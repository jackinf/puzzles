from typing import List


class Solution:
    """
    https://leetcode.com/problems/intersection-of-two-arrays-ii/
    Accepted
    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index = 0
        combined = []
        while len(nums1) > index:
            nums1_val = nums1[index]
            if nums1_val in nums2:
                combined.append(nums1_val)
                nums2.pop(nums2.index(nums1_val))
                nums1.pop(index)
            else:
                index += 1
        return combined


if __name__ == "__main__":
    s = Solution()

    case_1_nums1 = [1,2,2,1]
    case_1_nums2 = [2,2]
    print(s.intersect(case_1_nums1, case_1_nums2))

    case_1_nums1 = [4,9,5]
    case_1_nums2 = [9,4,9,8,4]
    print(s.intersect(case_1_nums1, case_1_nums2))