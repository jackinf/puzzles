from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        p1, p2 = 0, 0
        slots1.sort()
        slots2.sort()

        while p1 < len(slots1) and p2 < len(slots2):
            s1, e1 = slots1[p1]
            s2, e2 = slots2[p2]

            if e2 <= s1:
                p2 += 1
                continue

            if e1 <= s2:
                p1 += 1
                continue

            start, end = max(s1, s2), min(e1, e2)
            curr_duration = end - start
            if curr_duration >= duration:
                return [start, start + duration]

            if s2 < s1 < e1 < e2 or s1 < s2 < e1 < e2:
                p1 += 1
            else:
                p2 += 1

        return []