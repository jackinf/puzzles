import heapq
from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # s = list(filter(lambda slot: slot[1] - slot[0] >= duration, slots1 + slots2))
        s = [(slot[0], slot[1]) for slot in slots1 + slots2 if slot[1] - slot[0] >= duration]
        heapq.heapify(s)
        while s:
            if heapq.heappop(s)[1] >= s[0][0] + duration:
                return [s[0][0], s[0][0] + duration]
        return []