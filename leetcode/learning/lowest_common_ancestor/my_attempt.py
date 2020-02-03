from leetcode.learning.max_depth_of_binary_tree import TreeNode


class Solution:
    """
    Accepted
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ino, pre = [], []

        def scan(node: TreeNode, ino, pre):
            if not node:
                return
            pre.append(node)
            scan(node.left, ino, pre)
            ino.append(node)
            scan(node.right, ino, pre)

        scan(root, ino, pre)
        HM = {x.val: (idx, x) for idx, x in enumerate(ino)}

        def solve(HM, pre):
            elem = pre.pop(0)
            a, a_elem = HM[elem.val]
            x1, x1_elem = HM[p.val]
            x2, x2_elem = HM[q.val]

            if a == x2 or a == x1 or x1 < a < x2 or x2 < a < x1:
                return a_elem
            else:
                return solve(HM, pre)

        return solve(HM, pre)