from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.sink_island(grid, i, j)
        return count

    def sink_island(self, grid, i, j):
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"

        for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            self.sink_island(grid, ni, nj)