from typing import List, Tuple
Path = List[Tuple[int, int, int]]


class Solution:
    def cherryPickup(self, grid: List[List[int]]):
        start = (0, 0)
        target_x, target_y = len(grid[0])-1, len(grid)-1
        target = (target_x, target_y)

        print(f'from {start} to {target}')
        results1 = []
        self.solve(grid, start, target, [(0, 0, grid[0][0])], results1)

        print(f'from {target} to {start}')
        results2 = []
        self.solve(grid, target, start, [(target_x, target_y, grid[target_y][target_x])], results2)

        print(f'results1')
        for result1_item in results1:
            print(result1_item)

        print(f'results2')
        for results2_item in results2:
            print(results2_item)

    def solve(self, grid: List[List[int]], current: Tuple[int, int], target: Tuple[int, int], path: Path, results: List[Path]):
        x, y = current
        target_x, target_y = target
        # print(f'[{x},{y}], path: {path}')
        if x == target_x and y == target_y:
            results.append(path)
            # score = sum([x[2] for x in path])
            # print(f'path: {path}, score: {score}')
            return

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for dir_x, dir_y in directions:
            new_x, new_y = x + dir_x, y + dir_y
            # if x == 0 and y == 0 and new_x == 0 and new_y == 1:
            #     print(f'visited: {visited}')
            if self.is_visitable(grid, new_x, new_y, path):
                # print(f'({x},{y}), trying new_x: {new_x}, new_y: {new_y}, score: {grid[new_y][new_x]}')
                self.solve(grid, (new_x, new_y), target, path+[(new_x, new_y, grid[new_y][new_x])], results)

    def get_visited_index(self, x: int, y: int, row_len: int):
        return y * row_len + x

    def is_visitable(self, grid: List[List[int]], x: int, y: int, path: Path):
        if 0 > x or x >= len(grid[0]):
            return False
        if 0 > y or y >= len(grid):
            return False
        if grid[y][x] == -1:
            # print(f'Can\'t access [{x},{y}]')
            return False
        for path_x, path_y, score in path:
            if path_x == x and path_y == y:
                # print(f'Already visited [{x},{y}]')
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    test_case_1 = ([[0, 1, -1],
            [1, 0, -1],
            [1, 1, 1]], 5)

    s.cherryPickup(test_case_1[0])