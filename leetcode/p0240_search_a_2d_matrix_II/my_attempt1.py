class Solution:
    """
    Wrong answer
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        M, N = len(matrix[0]), len(matrix)
        seen_rows, seen_cols = set(), set()

        def search_row(i: int):
            seen_rows.add(i)
            diff = float('inf')

            # check if the value is in the row by checking min and max
            if not (matrix[i][0] <= target <= matrix[i][-1]):
                if i == N - 1:
                    return False
                return search_row(i + 1)

            prev_j = 0
            for j in range(M):
                if j in seen_cols:
                    continue

                new_diff = abs(target - matrix[i][j])
                if new_diff == 0:
                    return True
                elif new_diff < diff:
                    diff = new_diff
                    prev_j = j
                else:
                    return search_col(prev_j)
            return False

        def search_col(j: int):
            seen_cols.add(j)
            diff = float('inf')

            # check if the value is in the col by checking min and max
            if not (matrix[0][j] <= target <= matrix[-1][j]):
                if j == M - 1:
                    return False
                return search_col(j + 1)

            prev_i = 0
            for i in range(N):
                if i in seen_rows:
                    continue

                new_diff = abs(target - matrix[i][j])
                if new_diff == 0:
                    return True
                elif new_diff < diff:
                    diff = new_diff
                    prev_i = i
                else:
                    return search_row(prev_i)
            return False

        return search_row(0)