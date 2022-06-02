"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k
times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.
"""
from typing import List
# O(row * col)
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])

        def posToVal(r, c):
            return r * C + c  # position if in 1-dimensional array
        def valToPos(v):
            return [v//C, v%C]  # position in 2-dimensional array

        result = [[0] * C for i in range(R)]
        for r in range(R):
            for c in range(C):
                newPos = (posToVal(r, c) + k) % (R * C)
                newR, newC = valToPos(newPos)
                result[newR][newC] = grid[r][c]
        return result

grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
print(Solution().shiftGrid(grid, k))
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
