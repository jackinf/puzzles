from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.end = False


class WordDictionary:
    """
    Accepted
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.trie
        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.search_inner(word, self.trie, 0)

    def search_inner(self, word: str, curr: Trie, start: int):
        for i in range(start, len(word)):
            w = word[i]

            if w == ".":
                for k in curr.children:
                    child = curr.children[k]
                    if self.search_inner(word, child, i + 1):
                        return True

            if w not in curr.children:
                return False

            curr = curr.children[w]

        return curr.end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)