from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        cc = self.create_cc(accounts)
        g = self.create_graph(accounts, cc)

        seen = set()
        res = []
        for i in range(len(accounts)):
            name = accounts[i][0]
            s = set()
            self.dfs(accounts, g, name, i, seen, s)
            if s:
                res.append(sorted([name] + list(s)))

        return res

    def create_cc(self, accounts):
        cc = {}
        for i in range(len(accounts)):
            name = accounts[i][0]
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                cc[(name, email)] = i
        return cc

    def create_graph(self, accounts, cc):
        g = defaultdict(set)
        for i in range(len(accounts)):
            name = accounts[i][0]
            if not g[(name, i)]:
                g[(name, i)] = set()
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                x = cc[(name, email)]
                if x != i:
                    g[(name, i)].add(x)
                    g[(name, x)].add(i)
        return g

    def dfs(self, accounts, graph, name, i, seen, s):
        if (name, i) in seen:
            return
        seen.add((name, i))

        for j in range(1, len(accounts[i])):
            email = accounts[i][j]
            s.add(email)

        for next_i in graph[(name, i)]:
            self.dfs(accounts, graph, name, next_i, seen, s)
