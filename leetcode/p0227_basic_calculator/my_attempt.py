class Solution:
    def calculate(self, s: str) -> int:
        stack, p, res, count = [], 0, 0, 0
        s = s.replace(' ', '')  # todo: optimize

        def calculate(num1, num2, op):
            if op == "+": return num1 + num2
            elif op == "-": return num1 - num2
            elif op == "*": return num1 * num2
            elif op == "/": return num1 // num2
            raise Exception("operation not supported")

        for p in range(len(s)):
            if not s[p].isdigit():
                stack.append(s[p])
                continue

            count += 1
            if p + 1 < len(s) and s[p + 1].isdigit():
                continue

            print(p, count, p - count)
            num = int(s[1+p - count:1+p])
            count = 0

            if stack and (stack[-1] == "*" or stack[-1] == "/"):
                prev_op = stack.pop()
                prev_num = stack.pop()
                num = calculate(prev_num, num, prev_op)
            stack.append(num)

        stack = stack[::-1]
        n1 = stack.pop()
        while stack:
            op = stack.pop()
            n2 = stack.pop()
            n1 = calculate(n1, n2, op)
        return n1


if __name__ == "__main__":
    s = Solution()
    print(s.calculate("33+2*3-7"))
    print(s.calculate("0-1"))
    print(s.calculate("0-2147483647"))