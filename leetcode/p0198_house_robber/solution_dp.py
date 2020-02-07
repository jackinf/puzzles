from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
       # f(k) = max(f(k – 2) + Ak, f(k – 1))
        prev_max, curr_max = 0, 0
        for num in nums:
            temp = curr_max
            curr_max = max(prev_max + num, curr_max)
            prev_max = temp
        return curr_max


if __name__ == "__main__":
    s = Solution()

    print(s.rob([1, 2, 3, 1]))
    print(s.rob([2, 7, 9, 3, 1]))
    print(s.rob(
        [155, 44, 52, 58, 250, 225, 109, 118, 211, 73, 137, 96, 137, 89, 174, 66, 134, 26, 25, 205, 239, 85, 146, 73,
         55, 6, 122, 196, 128, 50, 61, 230, 94, 208, 46, 243, 105, 81, 157, 89, 205, 78, 249, 203, 238, 239, 217, 212,
         241, 242, 157, 79, 133, 66, 36, 165]))