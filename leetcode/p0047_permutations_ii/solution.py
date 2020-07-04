from collections import Counter


class Solution:
    """
    Not mine
    """
    def permuteUnique(self, nums):
        def btrack(path, counter):
            if len(path) == len(nums):
                ans.append(path[:])
            for x in counter:  # don't pick duplicates
                if counter[x] > 0:
                    path.append(x)
                    counter[x] -= 1
                    btrack(path, counter)
                    path.pop()
                    counter[x] += 1
        ans = []
        btrack([], Counter(nums))
        return ans