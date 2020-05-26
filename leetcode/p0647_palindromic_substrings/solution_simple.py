class Solution:
    """
    https://www.youtube.com/watch?v=EIf9zFqufbU
    """
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        count = 0
        matrix = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            matrix[i][i] = 1
            count += 1

        for col in range(N):
            for row in range(col):
                # 2 letters
                if row == col - 1 and s[row] == s[col]:
                    matrix[row][col] = 1
                    count += 1
                # inner substring is palindrome and characters on the edge are equal
                elif matrix[row+1][col-1] == 1 and s[row] == s[col]:
                    matrix[row][col] = 1
                    count += 1
        return count


if __name__ == "__main__":
    print(Solution().countSubstrings("aabaaca"))
