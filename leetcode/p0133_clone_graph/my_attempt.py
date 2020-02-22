from collections import defaultdict

class Node:
    def __init__(self, val = 0, neighbors=None):
        if neighbors is None:
            neighbors = []
        self.val = val
        self.neighbors = neighbors


class Solution:
    """
    Accepted
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        self.cache = {}
        self.collect_cache(node)

        for i, (k, v) in enumerate(self.cache.items()):
            cnode = self.cache[k]
            for nei in k.neighbors:
                cnei = self.cache[nei]
                cnode.neighbors.append(cnei)

        return self.cache[node]

    def collect_cache(self, node: 'Node'):
        if node in self.cache:
            return

        self.cache[node] = Node(node.val)

        for nei in node.neighbors:
            self.collect_cache(nei)