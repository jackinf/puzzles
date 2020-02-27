from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for y in range(len(board)):
            for x in range(len(board[0])):
                count = self.countNeighbors(board, x, y)

                if board[y][x] == 1 and (0 <= count <= 1 or 4 <= count <= 8):
                    board[y][x] = 2
                if board[y][x] == 0 and count == 3:
                    board[y][x] = 3

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 2:
                    board[y][x] = 0
                elif board[y][x] == 3:
                    board[y][x] = 1

    def countNeighbors(self, board: List[List[int]], curr_x: int, curr_y: int) -> int:
        neighbours = 0

        for y in [curr_y - 1, curr_y, curr_y + 1]:
            for x in [curr_x - 1, curr_x, curr_x + 1]:
                if x < 0 or y < 0 or x >= len(board[0]) or y >= len(board):
                    continue
                if x == curr_x and y == curr_y:
                    continue

                if board[y][x] in [1, 2]:
                    neighbours += 1

        return neighbours


if __name__ == "__main__":
    s = Solution()

    stage1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    stage2 = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    s.gameOfLife(stage1)  # mutate stage1 to become stage2
    print(stage1 == stage2)