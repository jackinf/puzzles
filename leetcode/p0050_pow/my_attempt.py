class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        negative = n < 0

        # bruteforce:

        # p = 0
        # while abs(n) > p:
        #     res *= x
        #     p += 1

        dp = {0: 1, 1: x}

        def calc(nn):
            if nn in dp:
                return dp[nn]

            nnn = nn // 2
            leftover = nn % 2
            res1 = calc(nnn) * calc(nnn) * calc(leftover)
            dp[nn] = res1

            return res1

        res = calc(abs(n))

        return res if not negative else 1 / res


if __name__ == "__main__":
    print(Solution().myPow(2, 10))
    print(round(Solution().myPow(2.1, 3), 4))
    print(Solution().myPow(2, -2))