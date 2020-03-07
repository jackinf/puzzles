from typing import List


class Solution:
    """
    Accepted - fast solution!
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        for ROW in range(N // 2):
            MAX = N - 1 - ROW

            for k in range(MAX - ROW):
                n1 = matrix[ROW][ROW + k]
                n2 = matrix[ROW + k][MAX]
                n3 = matrix[MAX][MAX - k]
                n4 = matrix[MAX - k][ROW]

                matrix[ROW][ROW + k] = n4
                matrix[ROW + k][MAX] = n1
                matrix[MAX][MAX - k] = n2
                matrix[MAX - k][ROW] = n3