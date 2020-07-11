class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False

        diff = len(s) - len(t)
        if abs(diff) > 1:
            return False
        if diff == -1:
            s, t = t, s

        p1, p2, lives = 0, 0, 1
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
                continue

            if lives == 1:
                lives -= 1
                p1 += 1
                if diff == 0:
                    p2 += 1
                continue

            return False

        return True