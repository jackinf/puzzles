from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.bfs(grid)

    def dfs(self, grid: List[List[int]]) -> int:
        pass

    def bfs(self, grid: List[List[int]]) -> int:
        row_len = len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [False] * (len(grid) * row_len)
        visited[self.get_visited_index(0, 0, row_len)] = True
        queue = [(0, 0)]

        while queue:
            x, y = queue.pop(0)
            print(f'[{x}, {y}]', end=" ")

            for dir_x, dir_y in directions:
                new_x, new_y = x + dir_x, y + dir_y
                if not (0 <= new_x < len(grid[0])) or not (0 <= new_y < len(grid)):
                    continue
                visited_coord = self.get_visited_index(new_x, new_y, row_len)
                if not visited[visited_coord]:
                    queue.append((new_x, new_y))
                    visited[visited_coord] = True
        pass

    def get_visited_index(self, x: int, y: int, row_len: int):
        return y * row_len + x

if __name__ == "__main__":
    s = Solution()
    test_case_1 = ([[0, 1, -1],
            [1, 0, -1],
            [1, 1, 1]], 5)

    s.cherryPickup(test_case_1[0])