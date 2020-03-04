from collections import defaultdict
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        steps = amount // coins[-1]
        rest = amount % coins[-1]
        if rest == 0:
            return steps

        dp = defaultdict(int)

        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
                continue

            sums = [dp[i - x] for x in coins if (i - x in dp)]
            if sums:
                dp[i] = min(sums) + 1

        if amount not in dp:
            return -1
        return dp[amount]