from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]):
        # self.bfs(grid)
        # self.dfs(grid)
        self.solve(grid)

    def solve(self, grid: List[List[int]]):
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        row_len = len(grid[0])
        visited_start = [False] * (len(grid) * row_len)

        def visit(x: int, y: int, visited: List[bool]):
            if not self.is_visitable(grid, x, y):
                return []
            if y == len(grid) - 1 and y == row_len:
                return [(x, y)]
            results = []
            for dir_x, dir_y in directions:
                new_x, new_y = x + dir_x, y + dir_y
                if not self.is_visitable(grid, new_x, new_y):
                    continue
                visited_index = self.get_visited_index(new_x, new_y, row_len)
                if not visited[visited_index]:
                    visited[visited_index] = True
                    results.append(visit(new_x, new_y, visited[:]))
            return [x for y in results for x in y]

        routes = visit(0, 0, visited_start)
        print(routes)

    def dfs(self, grid: List[List[int]]):
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        route = []
        row_len = len(grid[0])
        visited = [False] * (len(grid) * row_len)

        def visit(x: int, y: int, acc: int):
            visited[self.get_visited_index(x, y, row_len)] = True
            if x == row_len -1 and y == len(grid) -1:
                raise Exception("finished")

            for dir_x, dir_y in directions:
                new_x, new_y = x + dir_x, y + dir_y
                if not self.is_visitable(grid, new_x, new_y):
                    continue
                if visited[self.get_visited_index(new_x, new_y, row_len)]:
                    continue
                visit(new_x, new_y, acc + grid[y][x])
            route.append((x, y))

        try:
            visit(0, 0, grid[0][0])
        except:
            print(route)

        print(route)

    def bfs(self, grid: List[List[int]]):
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