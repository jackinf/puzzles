from typing import List


class Trie:
    def __init__(self):
        self.nodes = {}
        self.end = False

    def add(self, word: str):
        curr = self
        for ch in word:
            if not ch in curr.nodes:
                curr.nodes[ch] = Trie()
            curr = curr.nodes[ch]
        curr.end = True

    def search(self, keyword):
        curr = self
        for ch in keyword:
            if not ch in curr.nodes:
                return []
            curr = curr.nodes[ch]

        res = []
        curr.find_word(keyword, res)
        return res

    def find_word(self, acc: str, res: List[str]):
        if len(res) >= 3:
            return
        if self.end:
            res.append(acc)

        for ch, node in self.nodes.items():
            node.find_word(acc + ch, res)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        head = Trie()
        for product in sorted(products):
            head.add(product)

        results = []
        for i in range(1, len(searchWord) + 1):
            keyword = searchWord[:i]
            result = head.search(keyword)
            results.append(result)

        return results


if __name__ == "__main__":
    print(Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))