from copy import deepcopy
from typing import List, Tuple


class Solution:
    def cherryPickup(self, grid: List[List[int]]):
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        visited[0][0] = True
        path = [(0, 0)]
        self.solve(grid, 0, 0, visited, path)

    def solve(self, grid: List[List[int]], x: int, y: int, visited: List[List[int]], path: List[Tuple[int, int]]):
        # print(f'[{x},{y}], path: {path}')
        if x == len(grid[0])-1 and y == len(grid)-1:
            print('path', path)
            return

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for dir_x, dir_y in directions:
            new_x, new_y = x + dir_x, y + dir_y
            # if x == 0 and y == 0 and new_x == 0 and new_y == 1:
            #     print(f'visited: {visited}')
            if self.is_visitable(grid, new_x, new_y, visited):
                # print(f'({x},{y}), trying new_x: {new_x}, new_y: {new_y}')
                visited_copy = deepcopy(visited)
                visited_copy[new_y][new_x] = True
                self.solve(grid, new_x, new_y, visited_copy[:], path+[(new_x, new_y)])

    def get_visited_index(self, x: int, y: int, row_len: int):
        return y * row_len + x

    def is_visitable(self, grid: List[List[int]], x: int, y: int, visited: List[List[int]]):
        if 0 > x or x >= len(grid[0]):
            return False
        if 0 > y or y >= len(grid):
            return False
        if grid[y][x] == -1:
            # print(f'Can\'t access [{x},{y}]')
            return False
        if visited[y][x]:
            # print(f'Already visited [{x},{y}]')
            return False
        return True

if __name__ == "__main__":
    s = Solution()
    test_case_1 = ([[0, 1, -1],
            [1, 0, -1],
            [1, 1, 1]], 5)

    s.cherryPickup(test_case_1[0])