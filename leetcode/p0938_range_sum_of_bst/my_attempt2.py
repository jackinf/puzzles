from leetcode.p0938_range_sum_of_bst.TreeNode import TreeNode


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ans = 0
        stack = []
        curr = root

        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                if L <= curr.val <= R:
                    ans += curr.val
                if curr.val > R:
                    break
                curr = curr.right
            else:
                break

        return ans