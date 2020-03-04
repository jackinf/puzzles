from typing import List


class Solution:
    """
    Accepted
    """
    def depthSum(self, nestedList: List['NestedInteger']) -> int:
        return self.dfs(nestedList, 1)

    def dfs(self, nestedList: List['NestedInteger'], depth: int) -> int:
        res = 0
        for item in nestedList:
            if item.isInteger():
                res += item.getInteger() * depth
            else:
                res += self.dfs(item.getList(), depth + 1)
        return res