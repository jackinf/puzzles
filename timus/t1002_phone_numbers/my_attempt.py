import sys


class Solution:
    def solve(self, s: str, words):
        aaa = {"i": 1, "j": 1, "a": 2, "b": 2, "c": 2, "d": 3, "e": 3, "f": 3,
               "g": 4, "h": 4, "k": 5, "l": 5, "m": 6, "n": 6, "p": 7, "r": 7, "s": 7, "t": 8, "u": 8, "v": 8,
               "w": 9, "x": 9, "y": 9, "o": 0, "q": 0, "z": 0}
        self.translations = {}
        self.keys = []
        for word in words:
            key = "".join([str(aaa[x]) for x in word])
            self.translations[key] = word
            self.keys.append(key)

        self.scanned = [False] * len(s)
        ans = []
        if self.dfs(s, 0, ans):
            return " ".join(ans[::-1])
        else:
            return "No solution."

    def dfs(self, s: str, pointer: int, ans):
        if len(s) == pointer:
            return True
        if self.scanned[pointer]:
            return False

        for key in self.keys:
            if s.startswith(key, pointer) and self.dfs(s, len(key) + pointer, ans):
                ans.append(self.translations[key])
                return True

        self.scanned[pointer] = True
        return False


while True:
    sol = Solution()
    s = input()
    if s == "-1":
        sys.exit()
    words = []
    how_many = int(input())
    for i in range(how_many):
        words.append(input())
    print(sol.solve(s, words))


# input:
"""
7325189087
5
it
your
reality
real
our
4294967296
5
it
your
reality
real
our
-1
"""