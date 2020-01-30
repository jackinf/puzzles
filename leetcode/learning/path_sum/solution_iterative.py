class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False

        de = [(root, sum - root.val)]
        while de:
            node, remaining_sum = de.pop()
            if not node.left and not node.right and remaining_sum == 0:
                return True
            if node.left:
                de.append((node.left, remaining_sum - node.left.val))
            if node.right:
                de.append((node.right, remaining_sum - node.right.val))
        return False