from collections import Counter
import heapq


class Node:
    def __init__(self, letter: str, val: int):
        self.letter = letter
        self.val = val

    def __lt__(self, other):
        if self.val == other.val:
            return ord(self.letter) < ord(other.letter)
        return self.val < other.val

    def __repr__(self):
        return f'Node {self.letter}->{self.val}'


class Solution:
    def frequencySort(self, s: str) -> str:
        cc = Counter(s)
        arr = [Node(x, cc[x]) for x in s]
        heapq.heapify(arr)
        res = []
        while arr:
            res.append(heapq.heappop(arr).letter)
        return ''.join(res[::-1])


if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort("cccaaa"))