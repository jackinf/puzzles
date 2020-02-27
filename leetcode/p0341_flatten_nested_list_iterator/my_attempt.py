from typing import Union, List


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, val=Union[int, List['NestedInteger']]):
        self.val = val

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self.val, int)

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.val if self.isInteger() else None

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.val if isinstance(self.val, list) else None


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.LL: List[List[NestedInteger]] = [nestedList]
        self.next_int: int = self.findNext()

    def next(self) -> int:
        curr = self.next_int
        self.next_int = self.findNext()
        return curr

    def hasNext(self) -> bool:
        return self.next_int is not None

    def findNext(self) -> Union[int, None]:
        while self.LL:
            if not self.LL[-1]:
                self.LL.pop()
                continue

            node = self.LL[-1].pop(0)
            if node.isInteger():
                return node.getInteger()
            else:
                self.LL.append(node.getList())

        return None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


if __name__ == "__main__":
    p1 = NestedInteger([NestedInteger(1), NestedInteger(1)])
    p2 = NestedInteger(2)
    p3 = NestedInteger([NestedInteger(1), NestedInteger(1)])

    i, v = NestedIterator([p1, p2, p3]), []
    while i.hasNext(): v.append(i.next())
    print(v)