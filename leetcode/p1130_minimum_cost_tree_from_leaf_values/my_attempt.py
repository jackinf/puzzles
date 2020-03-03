from typing import List


class Solution:
    """
    Failed - wrong answer
    """
    def mctFromLeafValues(self, arr: List[int]) -> int:
        self.dp = {}
        self.arr = arr
        self.construct_dp(0, len(arr)-1)
        min_res = self.solve(0, len(arr)-1)
        return min_res

    def construct_dp(self, i: int, j: int):
        if i + 1 == j:
            self.dp[(i, j)] = self.arr[i] * self.arr[j]
            return max(self.arr[i], self.arr[j])

        right = self.construct_dp(i + 1, j)
        left = self.construct_dp(i, j - 1)
        self.dp[(i, j)] = right * left
        return max(right, left)

    def solve(self, i: int, j: int):
        if i == j:
            return 0
        if i + 1 == j:
            return self.dp[(i, j)]

        min_res = float('inf')
        for k in range(i, j):
            min_res = min(self.solve(i, k) + self.solve(k+1, j) + self.dp[(i, j)], min_res)
        return min_res


if __name__ == "__main__":
    s = Solution()
    print(s.mctFromLeafValues([6,2,4]))