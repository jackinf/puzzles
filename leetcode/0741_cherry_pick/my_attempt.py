from typing import List, Tuple


class Solution:
    def cherryPickup(self, grid: List[List[int]]):
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        self.solve(grid, 0, 0, visited, [])

    def solve(self, grid: List[List[int]], x: int, y: int, visited: List[List[int]], path: List[Tuple[int, int]]):
        print(x, y)
        if x == len(grid[0]) -1 and y == len(grid) -1:
            print('path', path)
            return

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for dir_x, dir_y in directions:
            new_x, new_y = x + dir_x, y + dir_y
            if self.is_visitable(grid, new_x, new_y) and not visited[y][x]:
                visited[new_x][new_y] = True
                self.solve(grid, new_x, new_y, visited[:], path+[(new_x, new_y)])


    def get_visited_index(self, x: int, y: int, row_len: int):
        return y * row_len + x

    def is_visitable(self, grid: List[List[int]], x: int, y: int):
        if not (0 <= x < len(grid[0])) or not (0 <= y < len(grid)) or grid[y][x] == -1:
            return False
        return True

if __name__ == "__main__":
    s = Solution()
    test_case_1 = ([[0, 1, -1],
            [1, 0, -1],
            [1, 1, 1]], 5)

    s.cherryPickup(test_case_1[0])