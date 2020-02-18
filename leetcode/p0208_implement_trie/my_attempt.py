class Trie:

    def __init__(self):
        self.list = []

    def insert(self, word: str) -> None:
        self.list.append(word)

    def search(self, word: str) -> bool:
        for item in self.list:
            if item == word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for item in self.list:
            if len(item) < len(prefix):
                continue

            found = True
            for i in range(len(prefix)):
                if item[i] != prefix[i]:
                    found = False
                    break

            if found:
                return True

        return False