# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root: return 0
        self.count = 0
        self.solve(root)
        return self.count

    def solve(self, node: TreeNode):
        if not node.left and not node.right:
            self.count += 1
            return True

        is_uni = True
        if node.left:
            is_uni = self.solve(node.left) and is_uni and node.val == node.left.val
        if node.right:
            is_uni = self.solve(node.right) and is_uni and node.val == node.right.val

        if is_uni:
            self.count += 1

        return is_uni