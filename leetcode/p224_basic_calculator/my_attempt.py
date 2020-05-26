from typing import Tuple


class Solution:
    """
    Accepted
    """
    def calculate(self, s: str) -> int:
        return self.calculateInner(s, 0)[0]

    def calculateInner(self, s: str, p: int) -> Tuple[int, int]:
        curr, res, op = 0, 0, 1

        while p < len(s):
            ch = s[p]
            p += 1

            if ch == " ":
                continue
            if ch.isnumeric():
                curr = curr * 10 + int(ch)
            else:
                res = res + curr * op
                curr = 0

            if ch == "+":
                op = 1
            if ch == "-":
                op = -1
            if ch == "(":
                curr, p = self.calculateInner(s, p)
                res = res + curr * op
                curr = 0
            if ch == ")":
                break

        res = res + curr * op
        curr = 0
        return (res, p)