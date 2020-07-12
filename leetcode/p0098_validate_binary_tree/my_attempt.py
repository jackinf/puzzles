# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        self.inorder(root, res)
        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True

    def inorder(self, node: TreeNode, res):
        if not node:
            return
        self.inorder(node.left, res)
        res.append(node.val)
        self.inorder(node.right, res)