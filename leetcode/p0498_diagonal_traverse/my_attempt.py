from typing import List


class Solution:
    """
    Accepted - very slow
    """
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res, steps = [], 0
        while matrix[-1]:
            if steps % 2 == 0:
                for step in range(min(steps, len(matrix))):
                    if matrix[step]:
                        res.append(matrix[step].pop(0))
            else:
                for step in range(min(steps, len(matrix)) - 1, -1, -1):
                    if matrix[step]:
                        res.append(matrix[step].pop(0))
            steps += 1

        return res