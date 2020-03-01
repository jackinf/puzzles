from typing import List


class Solution:
    def solve(self, arr: List[int], target: int):
        p1, p2 = 0, len(arr)-1
        while p1 <= p2:
            m = p1 + (p2-p1)//2
            if arr[m] == target:
                return arr[m]
            elif arr[m] < target:
                p1 = m+1
            elif arr[m] > target:
                p2 = m-1
        if p1 == 0:
            return -1
        return arr[p1-1]


if __name__ == "__main__":
    s = Solution()
    print(s.solve([1, 3, 5, 7, 9, 11, 13, 15], 14))
    print(s.solve([1, 3, 5, 7, 9, 11, 13, 15], 12))
    print(s.solve([1, 3, 5, 7, 9, 11, 13, 15], 10))
    print(s.solve([1, 3, 5, 7, 9, 11, 13, 15], 8))
    print(s.solve([1, 3, 5, 7, 9, 11, 13, 15], 6))
    print(s.solve([1, 3, 5, 7, 9, 11, 13, 15], 4))
    print(s.solve([1, 3, 5, 7, 9, 11, 13, 15], 2))
    print(s.solve([1, 3, 5, 7, 9, 11, 13, 15], 0))
    print(s.solve([7, 9, 11, 13, 15], 6))