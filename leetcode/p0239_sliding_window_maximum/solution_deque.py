from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        N = len(nums)
        if k >= N: return [max(nums)]

        deq = deque()

        def clean_deque(i):
            if deq and deq[0] == i-k:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # pre-start
        max_i = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            if nums[i] > nums[max_i]:
                max_i = i
        results = [nums[max_i]]

        # main part
        for i in range(k, N):
            clean_deque(i)
            deq.append(i)
            results.append(nums[deq[0]])

        return results


if __name__ == "__main__":
    print(Solution().maxSlidingWindow([-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7], 7))