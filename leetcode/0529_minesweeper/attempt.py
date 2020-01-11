from enum import Enum
from typing import List, Generator, Tuple


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        reveal_y, reveal_x = click

        current_cell: str = board[reveal_y][reveal_x]
        if current_cell == 'M':
            board[reveal_y][reveal_x] = 'X'
            return board  # game over

        def reveal(x: int, y: int):
            if current_cell == 'M':
                return
            elif current_cell == 'E':
                board[y][x] = 'B'
                neighbours = list(self.get_neighbours(board, x, y))
                mine_count = len([x for x in neighbours if x[2] == 'M'])
                if mine_count == 0:
                    for n_y, n_x, n_val in neighbours:
                        if n_val == 'E':
                            reveal(n_x, n_y)
                else:
                    board[y][x] = f'{mine_count}'

        reveal(reveal_x, reveal_y)
        return board

    def get_neighbours(self, board: List[List[str]], x: int, y: int) -> Generator[Tuple[int, int, str], None, None]:
        if y+1 < len(board):
            yield y+1, x, board[y+1][x]
        if y+1 < len(board) and x+1 < len(board[0]):
            yield y+1, x+1, board[y+1][x+1]
        if x+1 < len(board[0]):
            yield y, x+1, board[y][x+1]
        if y-1 >= 0 and x+1 < len(board[0]):
            yield y-1, x+1, board[y-1][x+1]

        if y-1 >= 0:
            yield y-1, x, board[y-1][x]
        if y-1 >= 0 and x-1 >= 0:
            yield y-1, x-1, board[y-1][x-1]
        if x-1 >= 0:
            yield y, x-1, board[y][x-1]
        if x-1 >= 0 and y+1 < len(board):
            yield y+1, x-1, board[y+1][x-1]

    def print_board(self, board: List[List[str]]):
        res = ""
        for line in board:
            res += "".join(line) + "\n"
        print(res)


if __name__ == "__main__":
    s = Solution()
    board = [['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'M', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E']]
    s.print_board(board)
    s.updateBoard(board, [3, 0])
    s.print_board(board)
