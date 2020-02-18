from typing import List


class Solution:
    """
    Accepted
    """
    def missingElement(self, nums: List[int], k: int) -> int:
        curr = nums[0]
        existing = nums.pop(0)

        while k > 0:
            if curr != existing:
                k -= 1
                if k == 0:
                    break
            else:
                if nums:
                    existing = nums.pop(0)
                else:
                    return curr + k
            curr += 1

        return curr