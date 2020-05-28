from typing import Tuple


class Solution:
    def solve(self, components: [Tuple[int, int]], player: [int, int]) -> str:
        def get_xdir(diff): return 'W' if diff < 0 else 'E' if diff > 0 else None
        def get_ydir(diff): return 'S' if diff < 0 else 'N' if diff > 0 else None

        moves = []
        for cx, cy in components:
            xdiff = cx - player[0]
            ydiff = cy - player[1]
            xdir = get_xdir(xdiff)
            ydir = get_ydir(ydiff)
            if xdir: moves.append((abs(xdiff), xdir))
            if ydir: moves.append((abs(ydiff), ydir))
            moves.append((1, 'P'))  # initiate a pickup
            player[0] = cx
            player[1] = cy

        return ''.join(list(map(str, [count*val for count, val in moves])))


"""
    Use this input:
2
2
1 1
0 0
1 0
    The output should be: NPWSP
"""
if __name__ == "__main__":
    grid_size = int(input())
    num_of_components = int(input())
    components = []
    for i in range(num_of_components):
        cx, cy = input().rstrip().split()
        components.append((int(cx), int(cy)))
    player = list(map(int, input().rstrip().split()))

    print(Solution().solve(components, player))
