from typing import List
import big_o


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans, left_max, right_max = 0, 0, 0
        left, right = 0, n-1

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.trap([4, 2, 3]))
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

    input_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
    best, others = big_o.big_o(s.trap, input_generator, n_repeats=1)
    print(best)
