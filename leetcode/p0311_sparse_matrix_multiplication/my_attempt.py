from typing import List


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

        N = len(A[0])  # A's col count is the same as B's row count

        a_rows_skip = [True] * len(A)
        b_cols_skip = [True] * len(B[0])

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    a_rows_skip[i] = False
                    break

        for j in range(len(B[0])):
            for i in range(len(B)):
                if B[i][j] != 0:
                    b_cols_skip[j] = False
                    break

        for i in range(len(A)):
            if a_rows_skip[i]: continue
            for j in range(len(B[0])):
                if b_cols_skip[j]: continue
                for k in range(N):
                    res[i][j] += A[i][k] * B[k][j]

        return res


if __name__ == "__main__":
    A = [[1, 0, 0], [-1, 0, 3]]
    B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]

    print(Solution().multiply(A, B))