class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            return self.multiply(num2, num1)

        num1 = num1[::-1]
        num2 = num2[::-1]

        res, carry, decimal = 0, 0, 0
        for i in range(len(num1)):
            deci, decj = 10 ** i, 0
            resj = 0
            for j in range(len(num2)):
                decj = 10 ** j

                subres, carry = self.mul_single(int(num1[i]), int(num2[j]), carry)
                resj += subres * decj

            if carry > 0:
                resj += carry * decj * 10
                carry = 0

            res += resj * deci

        return str(res)

    def mul_single(self, a, b, carry):
        res = a * b + carry
        return res % 10, res // 10