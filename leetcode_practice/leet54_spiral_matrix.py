"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while left <= right and top <= bottom:
            # get every i in top row
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            # get every i in right col
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            # check loop end condition
            if not(left <= right and top <= bottom):
                break
            # get every i in bottom row
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            # get every i in left col
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1

        return result
            
            
        


# TEST
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().spiralOrder(matrix))
# Expected Output: [1,2,3,6,9,8,7,4,5]
