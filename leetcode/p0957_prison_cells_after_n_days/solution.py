from typing import List


class Solution:
    """
    Not my code
    """

    def nextDay(self, cells: List[int]):
        new_cells = [0] * len(cells)
        for i in range(1, 7):
            new_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
        new_cells[0] = 0
        new_cells[7] = 0
        return new_cells

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = dict()
        is_fast_forwarded = False

        while N > 0:
            if not is_fast_forwarded:
                state_key = tuple(cells)
                if state_key in seen:
                    print(state_key, N, seen[state_key])
                    N %= seen[state_key] - N
                    print(N)
                    is_fast_forwarded = True
                else:
                    seen[state_key] = N

            if N > 0:
                N -= 1
                cells = self.nextDay(cells)

        return cells