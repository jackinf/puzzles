import random


class RandomizedSet:
    """
    Wrong answer
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = {}
        self.vals = []
        self.p = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.keys:
            return False

        self.vals.append(val)
        self.keys[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.keys:
            return False

        ind = self.keys[val]
        self.vals[self.p], self.vals[ind] = self.vals[ind], self.vals[self.p]
        self.p += 1
        del self.keys[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # print(self.p, len(self.vals))
        ind = random.randint(self.p, len(self.vals) - 1)
        return self.vals[ind]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
