"""
Given an m x n 2D binary grid grid which represents a map of
'1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume all
four edges of the grid are all surrounded by water.

# Method 1 - DFS approach
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            # if no more land, quit
            if r < 0 or r >= len(grid) or \
                c < 0 or c >= len(grid[0]) or \
                grid[r][c] != '1':
                return
            # instead of marking the node visited, make it the water
            grid[r][c] = '0'

            # search east west north south
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # numIslands(grid: List[List[str]]) starts here
        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if(grid[r][c] == '1'):
                    dfs(r, c)
                    # increment count by one once all land was searched
                    island_count += 1
        return island_count

"""
from typing import List
import collections

# Method 2 - BFS approach
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if( r in range(len(grid)) and
                        c in range(len(grid[0])) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        visited = set()
        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    # increment count by one once all land was searched
                    island_count += 1
        return island_count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(Solution().numIslands(grid))