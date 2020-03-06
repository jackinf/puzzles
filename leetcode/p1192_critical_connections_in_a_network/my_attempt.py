from typing import List
from collections import defaultdict


class Solution:
    """
    Accepted (but slow)
    """
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g, unique_nodes = defaultdict(list), set()
        for frm, to in connections:
            g[frm].append(to)
            g[to].append(frm)
            unique_nodes.add(frm)
            unique_nodes.add(to)

        bridges: List[List[int]] = []

        self.g = g
        self.visited = [False] * len(unique_nodes)
        self.lows = [0] * len(unique_nodes)
        self.ids = [0] * len(unique_nodes)
        self.id = 0

        for node in unique_nodes:
            if not self.visited[node]:
                self.dfs(node, node, bridges)

        return bridges

    def dfs(self, at, parent, bridges) -> None:
        self.visited[at] = True
        self.lows[at] = self.ids[at] = self.id
        self.id += 1
        print(at, parent, self.lows, self.ids, self.visited)

        for to in self.g[at]:
            if to == parent:
                continue

            if self.visited[to]:
                self.lows[at] = min(self.lows[at], self.ids[to])
            else:
                self.dfs(to, at, bridges)
                self.lows[at] = min(self.lows[at], self.lows[to])
                if self.ids[at] < self.lows[to]:
                    bridges.append([at, to])


if __name__ == "__main__":
    s = Solution()
    print(s.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))