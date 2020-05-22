# https://www.geeksforgeeks.org/find-closest-element-binary-search-tree/
class TreeNode:
    val: int
    left: 'TreeNode'
    right: 'TreeNode'

    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diff = float('inf')
        self.res = None

    def solve(self, root: 'TreeNode', k: int):
        self.diff = float('inf')
        self.res = None
        self.dfs_efficient(root, k)
        return self.res

    def dfs_simple(self, node: 'TreeNode', k):
        if not node:
            return

        curr_diff = abs(node.val - k)
        if self.diff > curr_diff:
            self.res = node.val
            self.diff = curr_diff

        self.dfs_simple(node.left, k)
        self.dfs_simple(node.right, k)

    def dfs_efficient(self, node: 'TreeNode', k):
        if not node:
            return

        curr_diff = abs(node.val - k)
        if self.diff > curr_diff:
            self.res = node.val
            self.diff = curr_diff

        if self.diff == 0:
            return

        if k < node.val:
            self.dfs_simple(node.left, k)
        else:
            self.dfs_simple(node.right, k)


if __name__ == "__main__":
    n03 = TreeNode(3)
    n05 = TreeNode(5)
    n07 = TreeNode(7)
    n06 = TreeNode(6, left=n05, right=n07)
    n04 = TreeNode(4, left=n03, right=n06)
    n20 = TreeNode(20)
    n22 = TreeNode(22, left=n20)
    n17 = TreeNode(17, right=n22)
    root = TreeNode(9, left=n04, right=n17)

    print(Solution().solve(root, 4))
    print(Solution().solve(root, 18))
    print(Solution().solve(root, 12))
