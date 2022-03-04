"""
You are given a 0-indexed 8 x 8 grid board, where board[r][c] represents the
cell (r, c) on a game board. On the board, free cells are represented by '.',
white cells are represented by 'W', and black cells are represented by 'B'.

Each move in this game consists of choosing a free cell and changing it to the
color you are playing as (either white or black). However, a move is only legal
if, after changing it, the cell becomes the endpoint of a good line (horizontal,
vertical, or diagonal).

A good line is a line of three or more cells (including the endpoints) where
the endpoints of the line are one color, and the remaining cells in the middle
are the opposite color (no cells in the line are free). You can find examples
for good lines in the figure below:
"""
from typing import List

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        rows, cols = len(board), len(board[0])
        direction = [[1,0], [-1,0],[0,1],[0,-1],
                     [1,1], [-1,-1],[-1,1],[1,-1]]
        board[rMove][cMove] = color

        def legal(row, col, color, direc):
            dr, dc = direc
            row, col = row + dr, col + dc
            length = 1

            while (0 <= row < rows and 0 <= col < cols):
                length += 1
                if board[row][col] == ".":
                    return False
                if board[row][col] == color:
                    return length >= 3

                row, col = row + dr, col + dc
            return False

        for d in direction:
            if legal(rMove, cMove, color, d):
                return True
        return False
            
        



if __name__ == "__main__":
    board = [[".",".",".","B",".",".",".","."],
             [".",".",".","W",".",".",".","."],
             [".",".",".","W",".",".",".","."],
             [".",".",".","W",".",".",".","."],
             ["W","B","B",".","W","W","W","B"],
             [".",".",".","B",".",".",".","."],
             [".",".",".","B",".",".",".","."],
             [".",".",".","W",".",".",".","."]]
    rMove = 4
    cMove = 3
    color = "B"
    print(Solution().checkMove(board, rMove, cMove, color))
"""
Output: true
Explanation: '.', 'W', and 'B' are represented by the colors blue, white, and black respectively, and cell (rMove, cMove) is marked with an 'X'.
The two good lines with the chosen cell as an endpoint are annotated above with the red rectangles.

board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"
Output: false
Explanation: While there are good lines with the chosen cell as a middle cell, there are no good lines with the chosen cell as an endpoint.
"""
