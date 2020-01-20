class Solution(object):
    def cherryPickup(self, grid):
        N = len(grid)
        memo = [[[None] * N for _1 in range(N)] for _2 in range(N)]

        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2

            # check if we go out of bounds or hit the thorn
            if (N == r1 or N == r2 or N == c1 or N == c2 or
                    grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
            # check if we hit the last element
            elif r1 == c1 == N-1:
                return grid[r1][c1]
            elif memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]
            else:
                ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]

                p1_right_and_p2_right = dp(r1, c1+1, c2+1)
                p1_down_and_p2_right = dp(r1+1, c1, c2+1)
                p1_right_and_p2_down = dp(r1, c1+1, c2)
                p1_down_and_p2_down = dp(r1+1, c1, c2)
                ans += max(p1_down_and_p2_down, p1_right_and_p2_down, p1_down_and_p2_right, p1_right_and_p2_right)

            memo[r1][c1][c2] = ans
            # print(memo)
            return ans

        return max(0, dp(0, 0, 0))


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
