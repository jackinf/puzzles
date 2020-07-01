import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.arr = [0]
        for item in w:
            self.arr.append(self.arr[-1] + item)

    def pickIndex(self) -> int:
        x = random.random() * self.arr[-1]
        p1, p2 = 0, len(self.arr) - 1

        while p1 <= p2:
            mid = (p2 - p1) // 2 + p1
            if self.arr[mid] <= x < self.arr[mid + 1]:
                return mid
            elif self.arr[mid] > x:
                p2 = mid - 1
            else:
                p1 = mid + 1

        return -1


if __name__ == "__main__":
    operations = ["Solution", "pickIndex", "pickIndex", "pickIndex", "pickIndex", "pickIndex"]
    values = [[[1, 3]], [1], [1], [1], [0], [1]]
    random.seed(10)  # I've picked this randomly
    sol = None
    for op, v in zip(operations, values):
        if op == "Solution":
            sol = Solution(v[0])
        elif op == "pickIndex":
            print(sol.pickIndex(), '==', v[0])
