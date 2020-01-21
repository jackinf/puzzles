from typing import List, Tuple
Path = List[Tuple[int, int, int]]


class Solution:
    def cherryPickup(self, grid: List[List[int]]):
        start = (0, 0)
        target_x, target_y = len(grid[0])-1, len(grid)-1
        target = (target_x, target_y)

        if start == target:
            return grid[0][0]

        print(f'from {start} to {target}')
        results1 = []
        self.solve(grid, start, target, [(0, 0, grid[0][0])], results1)

        # remove 0's
        print('here')
        for i in range(len(results1)):
            results1[i] = sorted([x for x in results1[i] if x[2] == 1])

        res = 0
        for i in range(len(results1)):
            results1_item1 = results1[i]
            for j in range(len(results1)):
                results1_item2 = results1[j]
                if i != j:
                    res = max(sum([x[2] for x in set(results1_item1 + results1_item2)]), res)
        return res

    def solve(self, grid: List[List[int]], current: Tuple[int, int], target: Tuple[int, int], path: Path, results: List[Path]):
        x, y = current
        target_x, target_y = target
        if x == target_x and y == target_y:
            print(f'path: {path}')
            results.append(path)
            return

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for dir_x, dir_y in directions:
            new_x, new_y = x + dir_x, y + dir_y
            if self.is_visitable(grid, new_x, new_y, path):
                self.solve(grid, (new_x, new_y), target, path+[(new_x, new_y, grid[new_y][new_x])], results)

    def get_visited_index(self, x: int, y: int, row_len: int):
        return y * row_len + x

    def is_visitable(self, grid: List[List[int]], x: int, y: int, path: Path):
        if 0 > x or x >= len(grid[0]):
            return False
        if 0 > y or y >= len(grid):
            return False
        if grid[y][x] == -1:
            return False
        for path_x, path_y, score in path:
            if path_x == x and path_y == y:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    test_case_1 = [[0,1,-1],[1,0,-1],[1,1,1]]
    test_case_2 = [[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]

    s.cherryPickup(test_case_2)
