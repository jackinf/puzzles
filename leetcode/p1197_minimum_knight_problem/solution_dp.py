from functools import lru_cache
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # dp = {}
        @lru_cache(None)
        def DP(x: int, y: int):
            if x + y == 0:
                return 0
            if x + y == 2:
                return 2

            # if (x,y) in dp:
            #     return dp[(x,y)]
            res1 = DP(abs(x-1), abs(y-2))
            res2 = DP(abs(x-2), abs(y-1))
            res = min(res1, res2) + 1
            # dp[(x,y)] = res
            return res

        return DP(abs(x), abs(y))


if __name__ == "__main__":
    s = Solution()

    print(s.minKnightMoves(1, 1))
    print(s.minKnightMoves(4, 3))