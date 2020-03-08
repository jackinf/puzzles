class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.grid = [[' ' for _ in range(n)] for _ in range(n)]
        self.p1_moves_made = 0
        self.p2_moves_made = 0
        self.winner = 0
        self.n = n

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

        pl = 'X' if player == 1 else 'O'
        self.grid[row][col] = pl
        self.p1_moves_made += int(player == 1)
        self.p2_moves_made += int(player == 2)
        if self.p1_moves_made < self.n and self.p2_moves_made < self.n:
            return 0

        # check row
        found = True
        for i in range(len(self.grid[row])):
            if self.grid[row][i] != pl:
                found = False
                break
        if found:
            self.winner = player
            return player

        # check col
        found = True
        for i in range(len(self.grid)):
            if self.grid[i][col] != pl:
                found = False
                break
        if found:
            self.winner = player
            return player

        # check diagonals
        if row == col:
            found = True
            for i in range(len(self.grid)):
                if self.grid[i][i] != pl:
                    found = False
                    break
            if found:
                self.winner = player
                return player

        if row == len(self.grid) - 1 - col:
            found = True
            for i in range(len(self.grid)):
                if self.grid[i][len(self.grid) - 1 - i] != pl:
                    found = False
                    break
            if found:
                self.winner = player
                return player

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)