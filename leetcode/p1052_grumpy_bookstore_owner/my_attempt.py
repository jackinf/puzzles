from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # start calculating customer losses
        record_i, record, res, N = 0, 0, 0, len(customers)

        # try to find X days in a row when the number of customer losses is the biggest
        for i in range(N):
            if i < X:
                record = res = res + customers[i] * grumpy[i]
                continue
            res = res - customers[i - X] * grumpy[i - X] + customers[i] * grumpy[i]
            if res > record:
                record, record_i = res, i - X + 1

        # make not grumpy on most active moments
        for i in range(record_i, min(record_i + X, N)):
            grumpy[i] = 0

        # calculate total sum of total non grumpy customers
        final_res = 0
        for i in range(N):
            final_res += customers[i] * (1 - grumpy[i])

        return final_res


if __name__ == "__main__":
    print(Solution().maxSatisfied(
        [1, 0, 1, 2, 1, 1, 7, 5],
        [0, 1, 0, 1, 0, 1, 0, 1],
        3
    ))