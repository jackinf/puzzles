# Definition for a binary tree node.
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Accepted: 50%
    """
    def inorder(self, node: TreeNode, x: int, y: int):
        if not node:
            return

        self.inorder(node.left, x - 1, y + 1)
        self.nodes.append((x, y, node.val))
        self.inorder(node.right, x + 1, y + 1)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.nodes = []
        self.inorder(root, 0, 0)
        maps = defaultdict(list)

        res = []
        for x, y, val in sorted(self.nodes):
            maps[x].append(val)

        for val in maps.values():
            res.append(val)

        return res