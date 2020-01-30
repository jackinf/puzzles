class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        x = [0]

        def solve1(node: TreeNode, depth: int, x):
            if not node:
                return
            if not node.left and not node.right:
                x[0] = max(x[0], depth)
            solve1(node.left, depth + 1, x)
            solve1(node.right, depth + 1, x)


        def solve2(node: TreeNode) -> int:
            if not node:
                return 0
            left_ans = solve2(node.left)
            right_ans = solve2(node.right)
            return max(left_ans, right_ans) + 1

        return solve2(root)
        # solve1(root, 1, x)
        # return x[0]