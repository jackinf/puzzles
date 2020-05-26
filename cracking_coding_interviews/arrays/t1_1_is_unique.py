from collections import defaultdict


class Solution:
    def solve(self, str1: str) -> bool:
        # O(n) time, and O(n) space

        seen = defaultdict(bool)
        for s in str1:
            if seen[s]:
                return False
            seen[s] = True
        return True

    def solve1(self, str1: str) -> bool:
        # O(nlogn) time, and O(1) space
        seen = [False] * 26
        for s in str1:
            index = ord(s) - ord('a')
            if seen[index]:
                return False
            seen[index] = True
        return True


if __name__ == "__main__":
    print(Solution().solve1("abcdeaf"))
    print(Solution().solve1("abcdef"))