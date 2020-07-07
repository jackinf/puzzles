from typing import List


class Solution:
    """
    simplest solution
    """
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0

        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    count += 1
                    self.sinkShip(i, j, board)
        return count

    def sinkShip(self, i: int, j: int, board: List[List[str]]):
        board[i][j] = '.'
        for newi, newj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if len(board) > newi >= 0 and len(board[0]) > newj >= 0 and board[newi][newj] == 'X':
                self.sinkShip(newi, newj, board)