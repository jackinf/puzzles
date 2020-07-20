class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        copies = {}
        copies[node] = Node(node.val)
        q = [node]

        while q:
            curr = q.pop(0)
            for nei in curr.neighbors:
                if nei not in copies:
                    copies[nei] = Node(nei.val)
                    q.append(nei)
                copies[curr].neighbors.append(copies[nei])

        return copies[node]
