from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width = len(board[0])
        height = len(board)
        N = len(word) - 1

        def find(i, j, p, dp):
            # check bounds
            if i < 0 or i > height - 1 or j < 0 or j > width - 1:
                return False

            # check if next letter is correct
            if board[i][j] != word[p]:
                return False

            # skip seen cell; mark cell as seen
            if 10000000 * i + j in dp:
                return False

            # check if the last letter
            if p == N:
                dp.add(10000000 * i + j)
                return True

            # check neighbouring cells
            dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dirx, diry in dirs:
                if find(i + dirx, j + diry, p + 1, dp):
                    dp.add(10000000 * i + j)
                    return True

            return False

        # scan each cell
        for i in range(height):
            for j in range(width):
                dp = set()
                if find(i, j, 0, dp):
                    # if len(dp) == len(word):
                    print(dp)
                    return True

        return False


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