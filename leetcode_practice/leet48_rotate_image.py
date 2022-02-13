"""
You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise). You have to rotate the image in-place, which means you have
to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do
the rotation.
"""
from typing import List

class Solution:
    def rotate(self, matrix):
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in range(len(matrix)):
            matrix[r].reverse()
            
            
            
# TEST
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix)
print(matrix)
# Expected Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
