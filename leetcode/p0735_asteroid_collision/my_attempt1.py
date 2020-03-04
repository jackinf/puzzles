from typing import List


class Solution:
    """
    Accepted. Bad space solution
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) <= 1:
            return asteroids

        pos_stack = []
        neg_stack = []
        outer_neg = []

        def clash():
            diff = int(pos_stack[-1] + neg_stack[-1])
            if diff == 0:
                neg_stack.pop()
                pos_stack.pop()
            elif diff > 0:
                neg_stack.pop()
            else:
                pos_stack.pop()
                if not pos_stack:
                    outer_neg.append(neg_stack.pop())

        for ast in asteroids:
            if ast >= 0:
                pos_stack.append(ast)
            else:
                if not pos_stack:
                    outer_neg.append(ast)
                    continue
                neg_stack.append(ast)

            while pos_stack and neg_stack:
                clash()

        return outer_neg + neg_stack + pos_stack
