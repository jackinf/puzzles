from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        res = 0
        self.found = []

        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.found.clear()
                    self.kill_island(i, j, grid, 'S')

                    found_str = ''.join(self.found)
                    if found_str not in seen:
                        res += 1
                        seen.add(found_str)

        return res

    def kill_island(self, i, j, grid, direction):
        if grid[i][j] == 0:
            return

        grid[i][j] = 0

        self.found.append(direction)

        for new_i, new_j, new_direction in ((i - 1, j, 'U'), (i + 1, j, 'D'), (i, j - 1, 'L'), (i, j + 1, 'R')):
            if new_i < 0 or new_i == len(grid) or new_j < 0 or new_j == len(grid[0]):
                continue
            self.kill_island(new_i, new_j, grid, new_direction)

        self.found.append('X')


if __name__ == "__main__":
    input1 = [
        [0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0],
        [0,0,1,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,0,0],
        [0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,0],
        [1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1]
    ]
    print(Solution().numDistinctIslands(input1))  # outputs 15