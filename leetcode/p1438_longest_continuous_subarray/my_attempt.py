import heapq
from typing import List


class Solution:
    """
    Total failure.
    """
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0

        rem_st, maxheap, minheap = [], [], []
        p1, p2, largest = 0, 0, 1
        heapq.heappush(maxheap, -nums[0])
        heapq.heappush(minheap, nums[0])

        while p1 < len(nums) and p2 < len(nums):
            nmax = -maxheap[0]
            nmin = minheap[0]
            diff = abs(nmax - nmin)

            if diff <= limit:
                largest = max(largest, p2 - p1 + 1)
                p2 += 1
                if p2 < len(nums):
                    heapq.heappush(maxheap, -nums[p2])
                    heapq.heappush(minheap, nums[p2])
            else:
                rem_st.append(nums[p1])
                while rem_st and maxheap and minheap:
                    if rem_st[-1] == minheap[0]:
                        rem_st.pop()
                        heapq.heappop(minheap)
                    elif rem_st[-1] == -maxheap[0]:
                        rem_st.pop()
                        heapq.heappop(maxheap)
                    else:
                        break
                p1 += 1
        return largest