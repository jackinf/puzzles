from typing import List


class Solution:
    """
    Accepted. Slow.
    """
    def countSubstrings(self, s: str) -> int:
        self.seen = set()
        self.counter = 0
        self.backtrack(list(s), list(s)[::-1], 0, len(s) - 1)
        return self.counter

    def backtrack(self, ls: List[str], rev_ls: List[str], p1: int, p2: int):
        if (p1, p2) in self.seen:
            return
        self.seen.add((p1, p2))

        if ls == rev_ls:
            self.counter += 1

        if p1 == p2:
            return

        tmp, tmp1 = ls.pop(0), rev_ls.pop()
        self.backtrack(ls, rev_ls, p1 + 1, p2)
        ls.insert(0, tmp)
        rev_ls.append(tmp1)

        tmp, tmp1 = ls.pop(), rev_ls.pop(0)
        self.backtrack(ls, rev_ls, p1, p2 - 1)
        ls.append(tmp)
        rev_ls.insert(0, tmp1)
