class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.result = 0
        self.traverse(root)
        return self.result

    def traverse(self, node):
        min_res, max_res = node.val, node.val
        for child in [node.left, node.right]:
            if child:
                a, b = self.traverse(child)
                self.result = max(self.result, abs(node.val - a), abs(node.val - b))
                min_res = min(min_res, a)
                max_res = max(max_res, b)

        return min_res, max_res
