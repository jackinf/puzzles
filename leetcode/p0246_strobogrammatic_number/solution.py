class Solution:
    def isStrobogrammatic(self, nums: str) -> bool:
        maps = {("0", "0"), ("1", "1"), ("6", "9"), ("9", "6"), ("8", "8")}
        N = len(nums)
        for i in range(N//2+1):
            if (nums[i], nums[N-i-1]) not in maps:
                return False
        return True
