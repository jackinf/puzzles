# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.st = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root:
            self.st.append(root)
            root = root.left

    def next(self) -> int:
        topmost = self.st.pop(0)
        if topmost.right:
            self._leftmost_inorder(topmost.right)
        return topmost.val

    def hasNext(self) -> bool:
        return len(self.st) > 0