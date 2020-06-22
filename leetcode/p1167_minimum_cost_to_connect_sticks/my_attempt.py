import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if not sticks: return 0

        heapq.heapify(sticks)
        cost = 0
        curr = heapq.heappop(sticks)
        while sticks:
            curr += heapq.heappop(sticks)
            cost += curr
            if sticks and curr > sticks[0]:
                heapq.heappush(sticks, curr)
                curr = heapq.heappop(sticks)

        return cost