from typing import List
import big_o


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)

        left_max, right_max = [-1]*n, [-1]*n
        left_max[0] = height[0]
        right_max[-1] = height[-1]

        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])
        for i in range(n-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        for i in range(n):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.trap([4, 2, 3]))
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

    input_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
    best, others = big_o.big_o(s.trap, input_generator, n_repeats=1)
    print(best)
