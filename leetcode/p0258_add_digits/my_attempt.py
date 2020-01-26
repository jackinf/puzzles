class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum(int(x) for x in str(num))
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.addDigits(99))
    print(s.addDigits(78))