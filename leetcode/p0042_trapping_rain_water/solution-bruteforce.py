from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)

        for i in range(n):
            max_left, max_right = 0, 0
            for j in range(i, -1, -1):
                max_left = max(max_left, height[j])
            for j in range(i, n, 1):
                max_right = max(max_right, height[j])
            ans += min(max_left, max_right) - height[i]

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.trap([4, 2, 3]))
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
