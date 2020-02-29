class Solution:
    """
    Accepted
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        for i in range(len(matrix)):
            p1, p2 = 0, len(matrix[0]) - 1
            if not (matrix[i][0] <= target <= matrix[i][-1]):
                continue

            # print(matrix[i][0], matrix[i][-1])
            while p1 <= p2:
                m = p2 + (p1 - p2) // 2
                print(i, m)

                if matrix[i][m] == target:
                    return True
                elif matrix[i][m] < target:
                    p1 = m+1
                elif matrix[i][m] > target:
                    p2 = m-1

        return False


if __name__ == "__main__":
    s = Solution()

    matrix1 = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    print(s.searchMatrix(matrix1, 5))