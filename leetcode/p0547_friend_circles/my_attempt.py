from typing import List


class Solution:
    """
    Accepted - not bad.
    """
    def findCircleNum(self, M: List[List[int]]) -> int:
        circles, seen, q = 0, set(), []
        for i in range(len(M)):
            if i in seen:
                continue
            found = False
            q.append(i)
            while q:
                curr = q.pop(0)
                for j in range(len(M[0])):
                    if M[curr][j] == 1 and j not in seen:
                        seen.add(j)
                        found = True
                        if curr != j:
                            q.append(j)

            circles += int(found)
        return circles