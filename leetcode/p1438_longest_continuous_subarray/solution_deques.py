import collections
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for a in nums:
            while len(maxd) and maxd[-1] < a: maxd.pop()
            while len(mind) and mind[-1] > a: mind.pop()
            maxd.append(a)
            mind.append(a)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]: maxd.popleft()
                if mind[0] == nums[i]: mind.popleft()
                i += 1
        return len(nums)-i


if __name__ == "__main__":
    print(Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5))