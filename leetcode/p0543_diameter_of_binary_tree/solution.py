# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def traverse(node: TreeNode):
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1
        traverse(root)
        return self.ans