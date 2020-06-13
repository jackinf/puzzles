class Solution:
    def __init__(self) -> None:
        self.arr = {}

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.recurse(0, s)

    def recurse(self, i, s):
        if i == len(s): return 1
        if s[i] == '0': return 0
        if i == len(s)-1: return 1
        if i in self.arr: return self.arr[i]

        ans = self.recurse(i+1, s)
        if int(s[i:i+2]) <= 26:
            ans += self.recurse(i+2, s)

        self.arr[i] = ans
        return ans


if __name__ == "__main__":
    print(Solution().numDecodings("22623224"))  # should print 18