class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        copies = self.create_copies(node)

        res = []
        for copy_node, neighbors in copies.values():
            copy_node.neighbors = [copies[nei][0] for nei in neighbors]

        return copies[node][0]

    def create_copies(self, node: 'Node'):
        copies = {}
        q = [node]
        seen = set()

        while q:
            curr = q.pop(0)
            if curr in seen:
                continue
            seen.add(curr)
            copies[curr] = (Node(curr.val), curr.neighbors)

            for nei in curr.neighbors:
                q.append(nei)
        return copies