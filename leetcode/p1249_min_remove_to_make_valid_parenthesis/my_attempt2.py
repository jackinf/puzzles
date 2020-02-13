class Solution:
    """
    Accepted.
    """
    def minRemoveToMakeValid(self, s: str) -> str:
        print()
        if not s:
            return ""

        def solve(s_inner: str, start: str, end: str):
            counter = 0
            res = ""
            for i, letter in enumerate(s_inner):
                if letter == start:
                    counter += 1
                if letter == end:
                    counter -= 1
                    if counter == -1:
                        counter = 0
                        continue
                res += letter
            return res

        s1 = solve(s, "(", ")")
        print(f's1={s1}')

        s2 = solve(s1[::-1], ")", "(")
        print(f's2={s2[::-1]}')

        return s2[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(s.minRemoveToMakeValid("a)b(c)d"))
    print(s.minRemoveToMakeValid("))(("))
    print(s.minRemoveToMakeValid("(a(b(c)d)"))
    print(s.minRemoveToMakeValid("())()((("))