class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        st = [root]
        while st:
            curr = st.pop()
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
            curr.left = None
            curr.right = st[-1] if st else None