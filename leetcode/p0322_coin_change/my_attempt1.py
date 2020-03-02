from collections import defaultdict
from typing import List


class Solution:
    """
    Failed
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) == 1:
            return amount // coins[0] if amount % coins[0] == 0 else -1
        coins.sort()

        steps = amount // coins[-1]
        rest = amount % coins[-1]

        dp = defaultdict(int)
        frm = coins[0] - 1
        to = min(amount, coins[-1]) + 1
        for i in range(frm, to):
            prev_sum = -1
            for coin2 in coins:
                if i < coin2:
                    break
                if prev_sum == -1:
                    prev_sum = dp[i - coin2]
                    continue
                prev_sum = min(dp[i - coin2], prev_sum)
            dp[i] = prev_sum + 1

        print(dp)
        if dp[rest] == 0:
            return -1
        return dp[rest] + steps