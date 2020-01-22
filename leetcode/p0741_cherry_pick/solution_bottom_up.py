class Solution(object):
    def cherryPickup(self, grid):
        N = len(grid)
        dp = [[float('-inf')] * N for _ in range(N)]
        dp[0][0] = grid[0][0]
        for t in range(1, 2*N - 1):
            dp2 = [[float('-inf')] * N for _ in range(N)]
            for i in range(max(0, t-(N-1)), min(N-1, t) + 1):
                for j in range(max(0, t-(N-1)), min(N-1, t) + 1):
                    if grid[i][t-i] == -1 or grid[j][t-j] == -1:
                        continue
                    val = grid[i][t-i]
                    if i != j: val += grid[j][t-j]
                    dp2[i][j] = max(dp[pi][pj] + val
                                    for pi in (i-1, i) for pj in (j-1, j)
                                    if pi >= 0 and pj >= 0)
            dp = dp2
        return max(0, dp[N-1][N-1])


if __name__ == "__main__":
    s = Solution()
    test_case_1 = [
        [0,1,-1],
        [1,0,-1],
        [1,1,1]]
    test_case_2 = [
        [1,1,1,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,1],
        [1,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,1,1,1]]

    print(s.cherryPickup(test_case_2))