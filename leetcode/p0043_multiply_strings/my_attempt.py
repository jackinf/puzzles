class Solution:
    """
    Accepted
    """
    def multiply(self, num1: str, num2: str) -> str:
        mapper = {str(k):k for k in range(10)}
        res1, res2 = 0, 0
        for i, x in enumerate(num1[::-1]):
            res1 += 10**i * mapper[x]
        for i, x in enumerate(num2[::-1]):
            res2 += 10**i * mapper[x]
        return str(res1 * res2)