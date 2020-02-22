from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, summ = 0, 0
        cache = defaultdict(int)
        cache[0] = 1

        for num in nums:
            summ += num
            if summ - k in cache:
                count += cache[summ - k]
            cache[summ] += 1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([3, 2, 7, 0, 1, 6, 4], k=7))