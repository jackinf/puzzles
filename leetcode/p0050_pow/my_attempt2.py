import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = n < 0

        dp = {0: 1, 1: x, 2: x * x}

        def calc(nn):
            if nn in dp:
                return dp[nn]

            divider = round(math.sqrt(nn))
            nnn = nn // divider
            leftover = nn % divider

            res1 = calc(leftover)
            for i in range(divider):
                res1 *= calc(nnn)

            dp[nn] = res1
            return res1

        res = calc(abs(n))

        return res if not negative else 1 / res