"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that
are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
                

        # 1. capture unsurrounded regions (O -> T)
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and
                    r in [0, rows - 1] or
                    c in [0, cols - 1]):
                    capture(r, c)

        # 2. capture surrounded regions (O -> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # 3. uncapture unsurrounded regions(T -> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        


# TEST
board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]

Solution().solve(board)
print(board)
"""
Output: [["X","X","X","X"],
         ["X","X","X","X"],
         ["X","X","X","X"],
         ["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that
any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not
on the border and it is not connected to an 'O' on the border will be flipped to
'X'. Two cells are connected if they are adjacent cells connected horizontally
or vertically.
"""
