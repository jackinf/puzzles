import math
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        self.p = 0
        self.count = 0

        for i in range(len(chars)):
            if i == 0 or chars[i] != chars[i - 1]:
                self.setNums(chars)
                chars[self.p] = chars[i]
                self.p += 1
                self.count = 1
            else:
                self.count += 1

        self.setNums(chars)

        return self.p

    def setNums(self, chars):
        if self.count <= 1:
            return

        N = int(math.log10(self.count))
        while N >= 0:
            res = self.count // 10**N
            self.count %= 10**N
            chars[self.p] = str(res)
            self.p += 1
            N -= 1

        # or simpler:
        """
        for c in f"{self.count}":
        chars[self.p] = c
        self.p += 1
        """


if __name__ == "__main__":
    inp1 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    res1 = Solution().compress(inp1)
    print(inp1[:res1])