from leetcode.p0572_subtree_of_another_tree import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.dfs(t) in self.dfs(s)

    def dfs(self, n: TreeNode):
        if not n:
            return "N"
        return "#{}{}{}".format(n.val, self.dfs(n.left), self.dfs(n.right))