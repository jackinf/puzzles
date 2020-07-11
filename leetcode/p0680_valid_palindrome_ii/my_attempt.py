class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.validate(s, True) or self.validate(s, False)

    def validate(self, s: str, increase_p1: bool) -> bool:
        p1, p2, lives = 0, len(s) - 1, 1
        while p1 < p2:
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
                continue

            if lives == 1:
                lives -= 1
                if increase_p1:
                    p1 += 1
                else:
                    p2 -= 1
                continue

            return False
        return True