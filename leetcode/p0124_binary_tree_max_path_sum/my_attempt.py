# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    https://leetcode.com/problems/binary-tree-maximum-path-sum/
    Accepted.
    """
    def __init__(self):
        self.ans = float('-inf')

    def maxPathSum(self, root: TreeNode) -> float:
        self.traverse(root)
        return self.ans

    def traverse(self, node: TreeNode):
        if not node:
            return 0

        l = self.traverse(node.left)
        r = self.traverse(node.right)

        self.ans = max(self.ans, node.val, node.val + l, node.val + r, node.val + l + r)
        return max(node.val + l, node.val + r, node.val)