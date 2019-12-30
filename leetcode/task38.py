from pprint import pprint
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        stack = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        """
        Do not return anything, modify board in-place instead.
        """

        def intersection(l1, l2):
            return [value for value in l1 if value in l2]

        def getCandidates(i, j) -> List[int]:
            if board[i][j] != ".":
                return []

            row = stack[:]
            col = stack[:]
            grid = stack[:]
            for x in range(len(board[0])):
                elem = board[i][x]
                if elem != ".":
                    row.remove(elem)
            for x in range(len(board)):
                elem = board[x][j]
                if elem != ".":
                    col.remove(elem)
            grid_offset_x = int(i / 3) * 3
            grid_offset_y = int(j / 3) * 3
            for x in range(3):
                for y in range(3):
                    elem = board[grid_offset_x + x][grid_offset_y + y]
                    if elem != ".":
                        grid.remove(elem)
            res = intersection(row, intersection(col, grid))
            if len(res) == 1:
                board[i][j] = f"{res[0]}"
            return res

        has_empty_spaces = True
        while has_empty_spaces is True:
            has_empty_spaces = False
            for i in range(9):
                for j in range(9):
                    results = getCandidates(i, j)
                    if len(results) > 0:
                        has_empty_spaces = True


s = Solution()
input_1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(s.solveSudoku(input_1))
