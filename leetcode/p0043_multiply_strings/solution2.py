class Solution:
    def multiply(self, num1: str, num2: str):
        res = [0]*(len(num1)+len(num2))
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                res[i+j] += int(e1) * int(e2)
                res[i+j+1] += res[i+j] // 10
                res[i+j] %= 10

        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return ''.join([str(x) for x in reversed(res)])


if __name__ == "__main__":
    print(Solution().multiply("123", "456"))

# [8, 6, 3, 1, 0, 0]
# [8, 8, 4, 0, 1, 0]
# [8, 8, 0, 6, 5, 0]
