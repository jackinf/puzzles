from pprint import pprint


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"{": "}", "[": "]", "(": ")"}
        for char in list(s):
            if char == ' ':
                continue

            if char in dict:  # is it opening bracket
                stack.append(dict[char])
            else:
                expected_closing_bracket = stack.pop()
                if char != expected_closing_bracket:
                    return False
        return True


pprint(Solution().isValid("{ { } [ ] [ [ [ ] ] ] }"))
