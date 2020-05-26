from leetcode.p0572_subtree_of_another_tree import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.traverse(s, t)

    def equ(self, s: TreeNode, t: TreeNode):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.equ(s.left, t.left) and self.equ(s.right, t.right)

    def traverse(self, s: TreeNode, t: TreeNode):
        return s and (self.equ(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t))