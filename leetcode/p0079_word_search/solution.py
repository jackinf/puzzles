from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.width = len(board[0])
        self.height = len(board)
        self.board = board
        self.word = word

        for i in range(self.height):
            for j in range(self.width):
                if self.backtrack(i, j, 0):
                    return True
        return False

    def backtrack(self, i, j, p: int) -> bool:
        if i < 0 or i == self.height or j < 0 or j == self.width or self.word[p] != self.board[i][j]:
            return False

        if len(self.word) -1 == p:
            return True

        self.board[i][j] = "#"
        res = False
        for iOffset, jOffset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if self.backtrack(i + iOffset, j + jOffset, p+1):
                res = True
                break
        self.board[i][j] = self.word[p]
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.exist([["a","a"]], "aaa"), False)
    print(s.exist([["a","b"],["c","d"]], "cdba"), True)
    print(s.exist([["A","B","C","E"],
                   ["S","F","E","S"],
                   ["A","D","E","E"]], "ABCESEEEFS"), True)
    print(s.exist([["A","B","C","E"],
                   ["S","F","C","S"],
                   ["A","D","E","E"]], "ABCB"), False)
    print(s.exist([["A","B","C","E"],
                   ["S","F","C","S"],
                   ["A","D","E","E"]], "ABCCED"), True)