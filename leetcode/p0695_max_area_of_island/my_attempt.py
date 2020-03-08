from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        record = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    record = max(self.sink(row, col), record)
        return record

    def sink(self, row: int, col: int):
        if row < 0 or row >= len(self.grid) or col < 0 or col >= len(self.grid[0]) or self.grid[row][col] == 0:
            return 0

        self.grid[row][col], points = 0, 1

        for row_offset, col_offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            points += self.sink(row + row_offset, col + col_offset)
        return points


if __name__ == "__main__":
    print(Solution().maxAreaOfIsland(
        [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    ))