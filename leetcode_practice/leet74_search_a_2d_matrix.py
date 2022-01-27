"""
Write an efficient algorithm that searches for a value in
an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last
integer of the previous row.

"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                break

        if not (top <= bottom):
            return False
        row = (top + bottom) //2
        l, r = 0, cols -1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 10
print(Solution().searchMatrix(matrix, target))