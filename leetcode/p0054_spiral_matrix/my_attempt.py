from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        dirq = [0, 1, 2, 3]
        N = 4
        x, y = 0, 0

        i = 0
        res = []
        turned = False
        while matrix[y][x] is not None or turned:
            if matrix[y][x] is not None:
                res.append(matrix[y][x])
            matrix[y][x] = None
            dd = dirq[i % N]

            nx, ny = x, y
            if dd == 0:
                nx += 1
            if dd == 1:
                ny += 1
            if dd == 2:
                nx -= 1
            if dd == 3:
                ny -= 1

            if ny >= len(matrix) or nx >= len(matrix[0]) or matrix[ny][nx] is None:
                i += 1
                turned = not turned
            else:
                x = nx
                y = ny
                turned = False
        return res