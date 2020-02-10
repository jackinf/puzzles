# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        def traverse(node: TreeNode):
            if not node:
                return 0, 0
            left_max, left_record = traverse(node.left)
            right_max, right_record = traverse(node.right)

            curr_max = max(left_max, right_max) + 1
            curr_record = max(left_max + right_max + 1, left_record, right_record)

            return curr_max, curr_record

        _, record = traverse(root)
        return record - 1