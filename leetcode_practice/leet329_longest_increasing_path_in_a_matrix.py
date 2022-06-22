"""
Given an m x n integers matrix, return the length of the longest increasing
path in matrix. From each cell, you can either move in four directions: left,
right, up, or down. You may not move diagonally or move outside the boundary
(i.e., wrap-around is not allowed).
"""
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}  # (r, c) --> LIP

        def dfs(r, c, preVal):
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                matrix[r][c] <= preVal):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            result = 1
            result = max(result, dfs(r + 1, c, matrix[r][c]) + 1)
            result = max(result, dfs(r - 1, c, matrix[r][c]) + 1)
            result = max(result, dfs(r, c + 1, matrix[r][c]) + 1)
            result = max(result, dfs(r, c - 1, matrix[r][c]) + 1)

            dp[(r, c)] = result
            return result
    
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)

        return max(dp.values())
        
        
        
        

# TEST
matrix = [[3,4,5],
          [3,2,6],
          [2,2,1]]
print(Solution().longestIncreasingPath(matrix))
"""
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is
not allowed.
"""
