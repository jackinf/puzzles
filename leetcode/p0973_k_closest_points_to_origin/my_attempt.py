from typing import List


class Solution:
    """
    Accepted
    """
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:K]


if __name__ == "__main__":
    s = Solution()
    print(s.kClosest([[1,3],[-2,2]], 1))
    print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))