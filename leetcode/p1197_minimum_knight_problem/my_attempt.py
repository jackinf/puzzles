from typing import List, Tuple


class Solution:
    """
    Wrong.
    """
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        level, next_pos, curr_pos = 0, [(0, 0)], []

        offset = 1
        if x > 10 or y > 10:
            offset = max(x // 2, y // 2)
            x %= 4
            y %= 4

        while True:
            level += 1
            curr_pos = next_pos
            next_pos = []
            for (xx, yy) in curr_pos:
                for (next_x, next_y) in self.get_knights_moves(xx, yy):
                    if x == next_x and y == next_y:
                        if offset > 1:
                            return offset
                        return level
                    next_pos.append((next_x, next_y))
        return 0

    def get_knights_moves(self, x: int, y: int) -> List[Tuple[int, int]]:
        return [
            (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2)
        ]