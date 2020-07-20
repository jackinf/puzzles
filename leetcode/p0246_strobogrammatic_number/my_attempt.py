class Solution:
    def isStrobogrammatic(self, nums: str) -> bool:
        self.maps = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}
        N = len(nums)
        for i in range(N):
            num = nums[i]
            if self.maps.get(num, "-") != nums[N-i-1]:
                return False
        return True
