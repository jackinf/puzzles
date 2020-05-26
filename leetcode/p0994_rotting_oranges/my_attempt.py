from typing import List


class Solution:
    """
    Accepted & Optimal.
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        fresh, max_lvl = 0, 0

        # collect fresh vegetable count as well as starting positions of rotten
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col, 1))

        # do BFS: scan neighbours, and mark them as rotten as well
        # we don't need to continue if all rooten fruits have been
        # processed or all fresh have been found
        while q and fresh > 0:
            row, col, lvl = q.pop(0)
            max_lvl = max(max_lvl, lvl)

            # check neighours
            for next_row, next_col in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                # check for bounds
                if next_row < 0 or next_row == len(grid) or next_col < 0 or next_col == len(grid[0]):
                    continue

                if grid[next_row][next_col] == 1:
                    grid[next_row][next_col] = 2
                    fresh -= 1
                    q.append((next_row, next_col, lvl + 1))

        return -1 if fresh > 0 else max_lvl