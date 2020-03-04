from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.wordList = wordList
        self.endWord = endWord
        self.dp = defaultdict(list)
        self.pair_up()
        print(self.dp)
        res = self.solve(beginWord, 1)
        if res == float('inf'):
            return 0
        return res

    def pair_up(self):
        for word in self.wordList:
            self.dp[word] = [i for i, w in enumerate(self.wordList) if sum(a != b for a, b in zip(word, w)) == 1]

    def solve(self, word: str, depth: int):
        if word == self.endWord:
            return depth

        best = float('inf')
        # print(self.wordList, word, depth)
        # for w in self.get_candidates(word):
        for w in self.dp[word]:
            next_word = self.wordList[w]
            if next_word == "#":
                continue
            self.wordList[w] = "#" * len(next_word)
            best = min(self.solve(next_word, depth + 1), best)
            self.wordList[w] = next_word

        return best