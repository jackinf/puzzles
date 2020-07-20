from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        houses = 0
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    houses += 1
                    q.append((i, j, houses, 0))

        visited = [[[0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        seen = set()

        minres = float('inf')
        while q:
            i, j, house_nr, depth = q.pop(0)
            if (i, j, house_nr) in seen:
                continue
            seen.add((i, j, house_nr))
            visited[i][j][0] += depth
            visited[i][j][1] += 1
            if visited[i][j][1] == houses and depth != 0:
                minres = min(minres, visited[i][j][0])

            for ni, nj in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
                if ni < 0 or ni == len(grid) or nj < 0 or nj == len(grid[0]):
                    continue
                if (ni, nj, house_nr) in seen or grid[ni][nj] == 1 or grid[ni][nj] == 2:
                    continue
                q.append((ni, nj, house_nr, depth + 1))

        if minres == float('inf'):
            return -1
        return minres
