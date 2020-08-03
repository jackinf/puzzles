from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []

        """
        Intersection
        a #----# 
        b    #----#

        a      #----#
        b #------#

        a     #---#
        b   #--------#

        a.  #--------#
        b.     #---#

        No intersection
        a. #-------#
        b              #----#

        a.              #---#
        b. #--------#
        """

        res = []
        p1, p2 = 0, 0
        while p1 < len(A) and p2 < len(B):
            a_st, a_end = A[p1]
            b_st, b_end = B[p2]

            if a_end < b_st:
                p1 += 1
            elif b_end < a_st:
                p2 += 1
            else:
                int_st, int_end = max(a_st, b_st), min(a_end, b_end)
                res.append((int_st, int_end))
                if b_end > a_end:
                    p1 += 1
                else:
                    p2 += 1
        return res

