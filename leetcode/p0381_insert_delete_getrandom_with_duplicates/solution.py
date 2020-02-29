from collections import defaultdict
from random import choice


class RandomizedCollection:

    def __init__(self):
        self.idx = defaultdict(set)
        self.vals = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.idx[val].add(len(self.vals))
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if len(self.idx[val]) == 0:
            return False

        ind = self.idx[val].pop()
        last = self.vals[-1]

        self.idx[last].add(ind)
        self.idx[last].discard(len(self.vals) - 1)

        self.vals[ind] = last
        self.vals.pop()

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.vals)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()