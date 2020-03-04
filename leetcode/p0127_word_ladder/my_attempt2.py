from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        self.wordList = wordList
        self.endWord = endWord
        self.dp = defaultdict(list)
        self.best = float('inf')

        self.dp[beginWord] = self.get_candidates(beginWord)
        for word in self.wordList:
            self.dp[word] = self.get_candidates(word)

        self.solve(beginWord, 1)
        if self.best == float('inf'):
            return 0
        return self.best

    def solve(self, word: str, depth: int):
        if self.best <= depth:
            return

        if word == self.endWord:
            self.best = depth
            return

        for w in self.dp[word]:
            next_word = self.wordList[w]
            if next_word == "#":
                continue
            self.wordList[w] = "#"
            self.solve(next_word, depth + 1)
            self.wordList[w] = next_word

    def get_candidates(self, word: str):
        res = []
        for k, another in enumerate(self.wordList):
            hits = 1
            for i in range(len(word)):
                if word[i] != another[i]:
                    hits -= 1
            if hits == 0:
                res.append(k)
        return res
