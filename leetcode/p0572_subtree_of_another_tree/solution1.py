from leetcode.p0572_subtree_of_another_tree import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        sres, tres = [], []
        self.dfs(s, sres)
        self.dfs(t, tres)
        return "".join(tres) in "".join(sres)

    def dfs(self, n: TreeNode, res: [str]):
        if not n:
            res.append('N')
            return
        res.append('#{}'.format(n.val))
        self.dfs(n.left, res)
        self.dfs(n.right, res)