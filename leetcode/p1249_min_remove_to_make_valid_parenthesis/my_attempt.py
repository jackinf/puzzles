class Solution:
    """
    Wrong
    """
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ""

        p1, p2 = -1, len(s)
        start = ""
        end = ""

        while p1 < p2:
            while p1 < p2 <= len(s):
                p1 += 1
                if p1 == p2:
                    break
                if s[p1] == "(":
                    break
                if s[p1] != ")":
                    start += s[p1]

            while p2 > p1 >= 0:
                p2 -= 1
                if s[p2] != "(":
                    end = s[p2] + end
                if s[p2] == ")":
                    start += s[p1]
                    break

        return start + end


if __name__ == "__main__":
    s = Solution()
    print(s.minRemoveToMakeValid("lee(t(c)o)de)"))