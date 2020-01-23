class Master1:
    def __init__(self, secret: str):
        self.secret = secret

    def guess(self, word: str) -> int:
        matches = 0
        for i in range(len(word)):
            matches += 1 if word[i] == self.secret[i] else 0
        return matches