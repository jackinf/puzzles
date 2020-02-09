from typing import List


class Solution:
    """
    Accepted
    """
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        if not A or not B:
            return []
        aa = A.pop(0)
        bb = B.pop(0)

        while aa and bb:
            if aa[1] < bb[0]:
                aa = A.pop(0) if A else None
                continue
            if bb[1] < aa[0]:
                bb = B.pop(0) if B else None
                continue

            # B is further than A
            if aa[0] <= bb[0] and aa[1] <= bb[1] and aa[1] >= bb[0]:
                res.append([bb[0], aa[1]])
                aa = A.pop(0) if A else None

            # A is further than B
            elif aa[0] >= bb[0] and aa[1] >= bb[1] and aa[0] <= bb[1]:
                res.append([aa[0], bb[1]])
                bb = B.pop(0) if B else None

            # A inside B
            elif aa[0] >= bb[0] and aa[1] <= bb[1]:
                res.append([aa[0], aa[1]])
                aa = A.pop(0) if A else None

            # B inside A
            elif aa[0] <= bb[0] and aa[1] >= bb[1]:
                res.append([bb[0], bb[1]])
                bb = B.pop(0) if B else None

        return res