from collections import Counter


class Solution(object):
    def topKFrequent(self, words, k):
        count = Counter(words)
        print(count)
        candidates = count.keys()
        print(candidates)
        candidates = sorted(candidates, key = lambda w: (-count[w], w))
        print(candidates)
        return candidates[:k]


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))