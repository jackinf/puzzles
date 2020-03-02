from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
            print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    s = Solution()
    # print(s.coinChange([2,5,10,1], 27))
    print(s.coinChange([2,1], 6))
    print(s.coinChange([1,2], 6))