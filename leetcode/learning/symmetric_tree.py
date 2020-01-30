# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(a: TreeNode, b: TreeNode) -> bool:
            if not a and not b: return True
            if not a or not b: return False
            return a.val == b.val and is_mirror(a.left, b.right) and is_mirror(a.right, b.left)

        # return is_mirror(root, root)

        q = [root, root]
        while q:
            a = q.pop(0)
            b = q.pop(0)
            if not a and not b: continue
            if not a or not b: return False
            if a.val != b.val: return False
            q.append(a.left)
            q.append(b.right)
            q.append(a.right)
            q.append(b.left)
        return True
