# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.mainhead = TreeNode()
        head = self.mainhead

        st = []
        curr = root
        while st or curr:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                curr = st.pop()
                head.next = curr
                head = head.next
                curr = curr.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.mainhead.next
        self.mainhead = self.mainhead.next
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if not self.mainhead:
            return False
        if hasattr(self.mainhead, 'next') and self.mainhead.next is not None:
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()