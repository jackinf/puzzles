from typing import List


def depthSumInverse(self, nestedList: List['NestedInteger']) -> int:
    unweighted = 0
    weighted = 0
    while nestedList:
        nextLevel = []
        for item in nestedList:
            if item.isInteger():
                unweighted += item.getInteger()
            else:
                nextLevel.extend(item.getList())
        weighted += unweighted
        nestedList = nextLevel
    return weighted