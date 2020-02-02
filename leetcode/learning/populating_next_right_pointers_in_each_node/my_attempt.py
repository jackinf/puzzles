from leetcode.learning.populating_next_right_pointers_in_each_node.node import Node


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def solve(node: Node, level, levels):
            if node is None:
                return
            if level >= len(levels):
                levels.append([])

            levels[level].append(node)
            solve(node.left, level + 1, levels)
            solve(node.right, level + 1, levels)

        levels = []
        solve(root, 0, levels)
        for level in levels:
            for i in range(1, len(level)):
                level[i - 1].next = level[i]
        return root