class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def isValid(p: str) -> bool:
            counter = 0
            for ch in p:
                counter += 1 if ch == '(' else -1
                if counter < 0:
                    return False
            return counter == 0

        arr = list(s)
        while len(arr) > 1:
            tempLeft = s[1:]
            tempRight = str(list(s).pop())

            if isValid(str(tempLeft)):
                return len(tempLeft)
            if isValid(str(tempRight)):
                return len(tempRight)

            s = s[1:]

        return 0


s = Solution()
print(s.longestValidParentheses(')()())'))