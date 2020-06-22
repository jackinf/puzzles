# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        diff = float('inf')
        res = root.val
        q = [root]
        while q:
            curr = q.pop(0)
            if not curr:
                continue

            newdiff = curr.val - target

            if abs(newdiff) < diff:
                diff = abs(newdiff)
                res = curr.val

            if newdiff > 0:
                q.append(curr.left)
            elif newdiff < 0:
                q.append(curr.right)

        return res