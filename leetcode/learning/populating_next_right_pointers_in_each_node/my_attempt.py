class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


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


