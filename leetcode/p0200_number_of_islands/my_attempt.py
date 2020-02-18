from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        self.WIDTH = len(grid[0])
        self.HEIGHT = len(grid)
        self.grid = grid
        self.islands = {}

        island_count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1' and (x, y) not in self.islands:
                    island_count += 1
                    self.connect(x, y)

        return island_count

    def connect(self, x: int, y: int):
        if x < 0 or y < 0:
            return
        if x >= self.WIDTH or y >= self.HEIGHT or self.grid[y][x] == '0':
            return
        if (x, y) in self.islands:
            return
        self.islands[(x, y)] = True
        self.connect(x + 1, y)
        self.connect(x - 1, y)
        self.connect(x, y - 1)
        self.connect(x, y + 1)