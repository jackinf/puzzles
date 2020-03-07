from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, res = [], [0] * len(T)

        for i in range(1, len(T)):
            # print(i, T[i])
            while stack and T[stack[-1]] < T[i]:
                j = stack.pop()
                res[j] = i - j

            if T[i] - T[i - 1] > 0:
                res[i - 1] = 1
            else:
                stack.append(i - 1)

        return res


if __name__ == "__main__":
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))