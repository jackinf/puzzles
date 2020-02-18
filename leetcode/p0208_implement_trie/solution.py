from typing import Union


class TrieNode:
    def __init__(self):
        self.R = 26
        self.links: Union['TrieNode', None] = [None] * self.R
        self.is_end = False

    def contains_key(self, ch: str) -> bool:
        return not not self.links[ord(ch) - ord('a')]

    def get(self, ch: str) -> Union['TrieNode', None]:
        return self.links[ord(ch) - ord('a')]

    def put(self, ch: str, node: 'TrieNode'):
        self.links[(ord(ch) - ord('a'))] = node

    def set_end(self):
        self.is_end = True


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if not node.contains_key(letter):
                node.put(letter, TrieNode())
            node = node.get(letter)
        node.set_end()

    def searchPrefix(self, word: str) -> Union[TrieNode, None]:
        node = self.root
        for letter in word:
            if node.contains_key(letter):
                node = node.get(letter)
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return not not node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

