from typing import List


class Solution:
    """
    Accepted
    """
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        N = len(heights)
        while V > 0:
            curr = K

            # search at left
            for i in range(K - 1, -1, -1):
                if heights[i] > heights[curr]:
                    break
                elif heights[i] < heights[curr]:
                    curr = i

            # search at right
            for i in range(curr + 1, N):
                if heights[i] > heights[curr]:
                    break
                elif heights[i] < heights[curr]:
                    curr = i

            heights[curr] += 1
            V -= 1
        return heights


if __name__ == "__main__":
    print(Solution().pourWater([2,1,1,2,1,2,2], 4, 3))