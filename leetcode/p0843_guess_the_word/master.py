class Master:
    def __init__(self, secret: str):
        self.secret = secret

    def guess(self, other: str):
        matches = 0
        for i in range(len(other)):
            matches += 1 if self.secret[i] == other[i] else 0
        return matches