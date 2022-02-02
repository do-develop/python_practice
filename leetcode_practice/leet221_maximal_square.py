"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.
"""
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def search(r, c):
            if r >= rows or c >= cols:
                return 0
            if (r,c) not in cache:
                down = search(r+1, c)
                right = search(r, c+1)
                diag = search(r+1, c+1)
                cache[(r,c)] = 0

                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down, right, diag)
            return cache[(r,c)]
        search(0, 0)
        return max(cache.values()) ** 2
        


# TEST
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
print(Solution().maximalSquare(matrix))  # Expected Output: 4
