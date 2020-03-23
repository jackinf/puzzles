class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n
        self.winner = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if self.winner != 0:
            return self.winner

        score = 1 if player == 1 else -1
        self.rows[row] += score
        if abs(self.rows[row]) == self.n:
            self.winner = player
            return self.winner

        self.cols[col] += score
        if abs(self.cols[col]) == self.n:
            self.winner = player
            return self.winner

        if row == col:
            self.diag += score
            if abs(self.diag) == self.n:
                self.winner = player
                return self.winner

        if row == self.n - col - 1:
            self.anti_diag += score
            if abs(self.anti_diag) == self.n:
                self.winner = player
                return self.winner

        return self.winner

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)