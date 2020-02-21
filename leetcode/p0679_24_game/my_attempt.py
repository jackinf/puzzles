from itertools import permutations
from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        perms = permutations(nums)
        for perm in perms:
            results = []
            print(perm)

            for p in perm:
                if not results:
                    results.append(p)
                    continue

                new_results = []
                for res in results:
                    new_results.append(res+p)
                    new_results.append(res-p)
                    new_results.append(res*p)
                    new_results.append(res//p)
                results = new_results

            results = [round(res) for res in results]

            if 24 in results:
                return True

        return False




if __name__ == "__main__":
    s = Solution()
    # print(s.judgePoint24([4, 1, 8, 7]))
    # print(s.judgePoint24([1, 2, 1, 2]))
    # print(s.judgePoint24([1, 3, 4, 6]))
    print(s.judgePoint24([1, 9, 1, 2]))