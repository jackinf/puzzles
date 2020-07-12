from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []
        if not digits:
            return self.res

        self.buttons = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        self.traverse(digits, 0, "")
        return self.res

    def traverse(self, digits: str, p: int, curr: str):
        if p == len(digits):
            self.res.append(curr)
            return

        for letter in self.buttons[digits[p]]:
            self.traverse(digits, p + 1, curr + letter)