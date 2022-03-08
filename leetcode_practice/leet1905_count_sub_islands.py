"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's
(representing water) and 1's (representing land). An island is a group of 1's
connected 4-directionally (horizontal or vertical). Any cells outside of the
grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1
that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.
"""
# Solution intuition:
# perform DFS on grid2 and check grid1 subisland simultaneously
from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visited = set()

        def dfs(r,c):
            # check for land from grid2
            if (r < 0 or c < 0 or r == rows or c == cols or
                grid2[r][c] == 0 or (r,c) in visited):
                return True
            visited.add((r,c))
            # if land from grid2, compare with grid1
            result = True
            if grid1[r][c] == 0:
                result = False

            # dfs in four directions
            result = dfs(r+1, c) and result
            result = dfs(r-1, c) and result
            result = dfs(r, c+1) and result
            result = dfs(r, c-1) and result

            return result

        count = 0 # count sub island
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] and (r,c) not in visited and dfs(r, c):
                    count += 1
        return count



# TEST
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
print(Solution().countSubIslands(grid1, grid2))
"""
Output: 3
"""
