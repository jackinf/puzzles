from typing import List


class Solution:
    """
    My solution worked!
    """

    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid[0])
        N = len(grid)
        dp = [[None]*M for _ in range(N)]
        return self.solve(grid, (0, 0), (M, N), dp)

    def solve(self, grid, xy, MN, dp):
        x, y = xy
        M, N = MN

        if x == M or y == N:
            return float('inf')
        if dp[y][x]:
            return dp[y][x]
        if x == M - 1 and y == N - 1:
            dp[y][x] = grid[y][x]
            return grid[y][x]

        from_right = self.solve(grid, (x + 1, y), MN, dp)
        from_bottom = self.solve(grid, (x, y + 1), MN, dp)
        ans = grid[y][x] + min(from_right, from_bottom)
        dp[y][x] = ans
        return ans


if __name__ == "__main__":
    s = Solution()

    test_case_1 = [
        [1,3,1],
        [1,5,1],
        [4,2,1]]
    test_case_2 = [
        [7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
        [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
        [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
        [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
        [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
        [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
        [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
        [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
        [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
        [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
        [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
        [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]

    print(s.minPathSum(test_case_2))
