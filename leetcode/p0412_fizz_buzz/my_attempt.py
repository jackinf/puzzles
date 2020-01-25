from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            if i % 15 == 0:
                ans.append(f"FizzBuzz")
            elif i % 5 == 0:
                ans.append(f"Buzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            else:
                ans.append(f"{i}")
        return ans


if __name__ == "__main__":
    s = Solution()

    print(s.fizzBuzz(15))