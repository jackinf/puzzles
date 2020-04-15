from leetcode.p0938_range_sum_of_bst.TreeNode import TreeNode


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0
        self.dfs(root, L, R)
        return self.ans

    def dfs(self, node: TreeNode, L: int, R: int):
        if not node:
            return
        if L <= node.val <= R:
            self.ans += node.val

        self.dfs(node.left, L, R)
        self.dfs(node.right, L, R)