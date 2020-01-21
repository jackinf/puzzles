class Solution(object):
    def cherryPickup(self, grid):
        def bestpath(grid):
            N = len(grid)
            NINF = float('-inf')
            dp = [[NINF] * N for _ in range(N)]
            dp[-1][-1] = grid[-1][-1]
            for i in range(N-1, -1, -1):
                for j in range(N-1, -1, -1):
                    if grid[i][j] >= 0 and (i != N-1 or j != N-1):
                        new_val_of_col = dp[i+1][j] if i+1 < N else NINF
                        new_val_of_row = dp[i][j+1] if j+1 < N else NINF

                        dp[i][j] = max(new_val_of_col, new_val_of_row)
                        dp[i][j] += grid[i][j]

            print('aaa')
            for row in dp:
                for cell in row:
                    print("{:0>2}".format(cell), end=" ")
                print()

            if dp[0][0] < 0:
                return None

            ans = [(0, 0)]
            i = j = 0
            while i != N-1 or j != N-1:
                if j+1 == N or i+1 < N and dp[i+1][j] >= dp[i][j+1]:
                    i += 1
                else:
                    j += 1
                ans.append((i, j))
            return ans

        ans = 0
        path = bestpath(grid)

        for i, j in path:
            ans += grid[i][j]
            grid[i][j] = 0

        for i, j in bestpath(grid):
            ans += grid[i][j]

        return ans


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

    print(s.cherryPickup(test_case_1))
