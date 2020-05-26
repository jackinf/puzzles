from typing import List


class Solution:
    """
    Accepted
    """
    def longestOnes(self, A: List[int], K: int) -> int:
        k_left, counter, max_counter, p1, p2 = K, 0, 0, 0, -1
        while p1 + 1 < len(A) and p2 + 1 < len(A):
            if p1 == p2 or k_left > 0:
                p2 += 1
                counter += 1
                if A[p2] == 0:
                    k_left -= 1
                while p2 + 1 < len(A) and A[p2 + 1] == 1:
                    p2 += 1
                    counter += 1
                max_counter = max(counter, max_counter)
            else:
                if A[p1] == 0:
                    k_left += 1
                p1 += 1
                counter -= 1
            # print(p1, p2, k_left, counter, max_counter)

        return max_counter