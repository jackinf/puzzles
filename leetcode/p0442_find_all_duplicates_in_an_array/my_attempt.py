from collections import Counter
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [k for k,v in Counter(nums).items() if v == 2]