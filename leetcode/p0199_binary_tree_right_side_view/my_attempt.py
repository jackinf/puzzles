# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = [(root, 0)]
        levels = []

        while q:
            curr, d = q.pop(0)
            if len(levels) == d:
                levels.append(curr.val)
            else:
                levels[d] = curr.val

            if curr.left:
                q.append((curr.left, d + 1))
            if curr.right:
                q.append((curr.right, d + 1))

        return levels