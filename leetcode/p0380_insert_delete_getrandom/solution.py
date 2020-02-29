import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = {}
        self.vals = []

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

        # ind = self.keys[val]
        # self.vals[-1], self.vals[ind] = self.vals[ind], self.vals[-1]
        last_element, idx = self.vals[-1], self.keys[val]
        self.vals[idx], self.keys[last_element] = last_element, idx

        self.vals.pop()
        del self.keys[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.vals)
        # ind = random.randint(0, len(self.vals)-1)
        # return self.vals[ind]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()