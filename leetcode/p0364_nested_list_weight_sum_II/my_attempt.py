from typing import List, Tuple


class Solution:
    """
    Accepted
    """
    def depthSumInverse(self, nestedList: List['NestedInteger']) -> int:
        self.record = 1
        q = []
        self.dfs(nestedList, 1, q)

        res = 0
        for val, depth in q:
            res += (self.record - depth + 1) * val

        return res

    def dfs(self, nestedList: List['NestedInteger'], depth: int, q: List[Tuple[int, int]]):
        if self.record < depth:
            self.record = depth

        res = 0
        for item in nestedList:
            if item.isInteger():
                q.append((item.getInteger(), depth))
            else:
                self.dfs(item.getList(), depth + 1, q)