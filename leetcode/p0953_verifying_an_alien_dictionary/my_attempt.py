from typing import List


class Solution:
    """
    Accepted
    """
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True

        for i in range(len(words)-1):
            if self.is_first_word_bigger(words[i], words[i+1], order):
                return False
        return True

    def is_first_word_bigger(self, word1: str, word2: str, order: str) -> bool:
        min_N = min(len(word1), len(word2))
        for i in range(min_N):
            if order.index(word1[i]) > order.index(word2[i]):
                return True
            elif order.index(word1[i]) < order.index(word2[i]):
                return False

        # at this point, words are equal, compare sizes
        return len(word1) > len(word2)



if __name__ == "__main__":
    s = Solution()

    input1 = ["zirqhpfscx", "zrmvtxgelh", "vokopzrtc", "nugfyso", "rzdmvyf", "vhvqzkfqis", "dvbkppw", "ttfwryy", "dodpbbkp", "akycwwcdog"]
    order1 = "khjzlicrmunogwbpqdetasyfvx"
    print(s.isAlienSorted(input1, order1))