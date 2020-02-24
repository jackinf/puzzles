from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        res = 0

        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[0])):
                me = int(matrix[y][x])
                res = max(me, res)
                if int(me) == 0 or x == 0 or y == 0:
                    continue

                a = int(matrix[y - 1][x])
                b = int(matrix[y][x - 1])
                c = int(matrix[y - 1][x - 1])
                abc_min = min(a, b, c)

                if abc_min != 0:
                    matrix[y][x] = abc_min + 1
                    res = max(matrix[y][x], res)

        return res ** 2