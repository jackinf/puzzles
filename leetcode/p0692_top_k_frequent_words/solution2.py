from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))