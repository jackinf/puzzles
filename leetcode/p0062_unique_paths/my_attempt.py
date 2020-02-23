class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for y in range(m):
            for x in range(n):
                if x == 0 and y == 0:
                    continue
                top = dp[y - 1][x] if y > 0 else 0
                left = dp[y][x - 1] if x > 0 else 0

                dp[y][x] = top + left

        return dp[-1][-1]