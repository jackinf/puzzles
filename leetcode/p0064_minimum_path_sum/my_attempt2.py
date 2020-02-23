from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid)  # rows
        N = len(grid[0])  # columns

        for y in range(M):
            for x in range(N):
                if x == 0 and y == 0:
                    continue
                if x > 0 and y == 0:
                    grid[0][x] += grid[0][x - 1]
                elif y > 0 and x == 0:
                    grid[y][0] += grid[y - 1][0]
                else:
                    grid[y][x] += min(grid[y][x - 1], grid[y - 1][x])

        return grid[-1][-1]