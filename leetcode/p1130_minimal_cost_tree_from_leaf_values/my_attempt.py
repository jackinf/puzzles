from typing import List


class Solution:
    """
    Wrong answer
    """
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = {}

        def calc(p1, p2):
            if (p1, p2) in dp:
                return

            if p1 + 1 == p2:
                dp[(p1, p2)] = arr[p1] * arr[p2]

            if p2 < len(arr) - 1 and (p1, p2 + 1) not in dp:
                dp[(p1, p2 + 1)] = max(arr[p1:p2]) * arr[p2 + 1]
                calc(p1, p2 + 1)
            if p1 > 0 and (p1 - 1, p2) not in dp:
                dp[(p1 - 1, p2)] = max(arr[p1:p2]) * arr[p1 - 1]
                calc(p1 - 1, p2)

        for i in range(len(arr) - 1):
            calc(i, i + 1)
        # print(dp)

        def solve(p1, p2):
            res = dp[(p1, p2)]

            if p2 < len(arr) - 1 and p1 > 0:
                return res + min(solve(p1, p2 + 1), solve(p1 - 1, p2))
            if p2 < len(arr) - 1:
                return res + solve(p1, p2 + 1)
            if p1 > 0:
                return res + solve(p1 - 1, p2)
            return res

        min_sum = float('inf')
        for i in range(len(arr) - 1):
            min_sum = min(min_sum, solve(i, i + 1))

        return min_sum


if __name__ == "__main__":
    s = Solution()
    print(s.mctFromLeafValues([6,2,4]))