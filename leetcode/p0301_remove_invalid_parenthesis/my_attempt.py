from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        q = [(s, 0)]
        max_depth, results, seen = float('inf'), set(), set()
        while q:
            curr, d = q.pop(0)

            if curr in seen:
                continue
            seen.add(curr)

            if self.isValid(curr):
                max_depth = d
                results.add(curr)

            if d >= max_depth:
                continue

            for i in range(len(curr)):
                if curr[i] != "(" and curr[i] != ")":
                    continue
                q.append((curr[:i] + curr[i + 1:], d + 1))
        return results

    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if s[i] == "(":
                st.append(s[i])
            elif s[i] == ")":
                if not st:
                    return False
                st.pop()
        return len(st) == 0