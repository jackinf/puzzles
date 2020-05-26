class Solution:
    def calculate(self, s: str) -> int:
        res, operand, sign = 0, 0, 1
        stack = []

        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            elif ch == "+":
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == "-":
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                operand = 0
                res = 0
            elif ch == ")":
                res += sign * operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0
        res += sign * operand
        return res