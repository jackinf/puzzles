from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.found = False
        self.s = s
        self.wordDict = wordDict
        return self.solve(0, [False] * len(s))

    def solve(self, p1: int, scanned):
        if p1 == len(self.s):
            return True
        if scanned[p1]:
            return False

        for word in self.wordDict:
            if self.s.startswith(word, p1) and self.solve(p1 + len(word), scanned):
                return True

        scanned[p1] = True
        return False