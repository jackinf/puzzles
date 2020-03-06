from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [0] * len(M)
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                self.dfs(M, visited, i)
                count += 1
        return count

    def dfs(self, M: List[List[int]], visited: List[int], i: int):
        for j in range(len(M[0])):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, visited, j)


if __name__ == "__main__":
    s = Solution()
    print(s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
    print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))