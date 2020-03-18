from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        q = [(root, 0, 0)]
        res = defaultdict(list)
        while q:
            curr, lvl, hor = q.pop(0)
            res[hor].append(curr.val)
            if curr.left:
                q.append((curr.left, lvl+1, hor-1))
            if curr.right:
                q.append((curr.right, lvl+1, hor+1))
        return [y for x,y in sorted(res.items())]