"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row
and column to 0's, and return the matrix. You must do it in place.
"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        row_zero = False  # mark separately

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0
                    



# TEST
matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
Solution().setZeroes(matrix)
print(matrix)
# Expected Output: [[0,0,0,0],
#                   [0,4,5,0],
#                   [0,3,1,0]]
