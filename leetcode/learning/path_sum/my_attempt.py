# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        x = [False]
        def helper(node: TreeNode, temp_sum: int, x):
            if not node or x[0]:
                return
            if not node.left and not node.right:
                if temp_sum == sum:
                    x[0] = True
                return
            if node.left:
                helper(node.left, temp_sum + node.left.val, x)
            if node.right:
                helper(node.right, temp_sum + node.right.val, x)
        helper(root, root.val, x)
        return x[0]