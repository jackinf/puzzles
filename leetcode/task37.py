from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        stack = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # validate rows
        for row_i in range(len(board)):
            check = stack[:]
            check_1 = stack[:]
            for col_i in range(len(board[0])):
                elem = board[row_i][col_i]
                elem_1 = board[col_i][row_i]
                if elem in check:
                    check.remove(elem)
                elif elem != ".":
                    return False
                if elem_1 in check_1:
                    check_1.remove(elem_1)
                elif elem_1 != ".":
                    return False

        # validate sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check = stack[:]
                for x in range(3):
                    for y in range(3):
                        elem = board[i + x][j + y]
                        if elem in check:
                            check.remove(elem)
                        elif elem != ".":
                            return False

        return True




s = Solution()
input_1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(s.isValidSudoku(input_1))
