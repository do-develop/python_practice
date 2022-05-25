"""
You are given row x col grid representing a map where grid[i][j] = 1 represents
land and grid[i][j] = 0 represents water. Grid cells are connected horizontally/
vertically (not diagonally). The grid is completely surrounded by water, and
there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to
the water around the island. One cell is a square with side length 1. The grid
is rectangular, width and height don't exceed 100. Determine the perimeter of
the island.
"""
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(r, c):
            # base case 1 - add parameter
            if r >= len(grid) or c >= len(grid[0]) or \
               r < 0 or c < 0 or grid[r][c] == 0:
                return 1
            # base case 2 - already visited
            if (r, c) in visit:
                return 0

            visit.add((r, c))
            perim = dfs(r, c + 1)
            perim += dfs(r + 1, c)
            perim += dfs(r, c - 1)
            perim += dfs(r - 1, c)

            return perim

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    return dfs(r, c)


# TEST
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(Solution().islandPerimeter(grid))
# expected output: 16
        
