from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) <= 1:
            return asteroids

        st, p = [], 0
        while p < len(asteroids):
            if asteroids[p] < 0 and st and st[-1] > 0:
                diff = asteroids[p] + st[-1]
                if diff == 0:
                    st.pop()
                elif diff < 0:
                    st.pop()
                    continue
            else:
                st.append(asteroids[p])
            p += 1

        return st