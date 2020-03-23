from collections import defaultdict
from typing import List


class Solution:
    NOT_VISITED = 0
    VISITING = 1
    VISITED = 2

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.coll = defaultdict(list)
        self.stack = []
        self.visited = [0] * numCourses
        self.is_possible = True

        for target, source in prerequisites:
            self.coll[source].append(target)

        for i in range(numCourses):
            if self.visited[i] == Solution.NOT_VISITED:
                self.dfs(i)

        if not self.is_possible:
            return []
        return self.stack

    def dfs(self, i):
        if self.visited[i] == Solution.VISITING:
            return

        self.visited[i] = Solution.VISITING
        for item in self.coll[i]:
            if self.visited[item] == Solution.NOT_VISITED:
                self.dfs(item)
            elif self.visited[item] == Solution.VISITING:
                self.is_possible = False
                return
        self.visited[i] = Solution.VISITED
        self.stack.insert(0, i)
