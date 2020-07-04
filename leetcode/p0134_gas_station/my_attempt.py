from typing import List


class Solution:
    """
    Very slow
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        N = len(gas)
        for i in range(N):
            tank = gas[i]
            fail = False

            for j in range(N):
                prev = (i + j) % N
                curr = (i + j + 1) % N
                tank -= cost[prev]
                if tank < 0:
                    fail = True
                    break
                tank += gas[curr]

            if not fail:
                return i

        return -1