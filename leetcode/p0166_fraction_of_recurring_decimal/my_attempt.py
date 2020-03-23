import math


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        steps, res, ans = 0, numerator, 0
        before = math.ceil(math.log10(numerator/denominator))
        print(before)
        while steps < 10:
            ans, rest = divmod(res, denominator)
            print(ans, res, steps, ans%(10**(before + steps - 1)))
            res *= 10
            steps += 1

        print(ans)

if __name__ == "__main__":
    s = Solution()
    s.fractionToDecimal(72, 13)
    # s.fractionToDecimal(1, 2)