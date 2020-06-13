import heapq
from typing import List


class MaxHeap:
    def __init__(self):
        self.arr = []

    def push(self, val):
        heapq.heappush(self.arr, -val)

    def pop(self):
        return -1 * heapq.heappop(self.arr) if self.arr else None

    def peek(self):
        return -1 * self.arr[0] if self.arr else None

    def has_elements(self):
        return len(self.arr) > 0


class Solution:
    """
    Not very fast but it got accepted. Time complexity is O(Nlog(k))
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return [max(nums)]

        results = []
        remheap = MaxHeap()
        heap = MaxHeap()

        # scan first k elements
        for i in range(k):
            heap.push(nums[i])
        results.append(heap.peek())

        # main part: scan elements using sliding window
        for i in range(k, len(nums)):
            L = nums[i - k]
            R = nums[i]

            remheap.push(L)
            while remheap.has_elements() and heap.has_elements() and remheap.peek() == heap.peek():
                remheap.pop()
                heap.pop()

            heap.push(R)
            results.append(heap.peek())

        return results


if __name__ == "__main__":
    print(Solution().maxSlidingWindow([-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7], 7))