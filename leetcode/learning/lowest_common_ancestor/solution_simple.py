from leetcode.learning.max_depth_of_binary_tree import TreeNode


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def solve(node: TreeNode):
            if not node:
                return False

            r1 = solve(node.left)
            r2 = solve(node.right)
            mid = node.val == p.val or node.val == q.val

            if r1 + r2 + mid >= 2:
                self.ans = node
            return mid or r1 or r2

        solve(root)
        return self.ans