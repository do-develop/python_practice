class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        # DFS approach
        def dfs(r, c):
            grid[r][c] = 0
            # from here go 4 directions
            for x, y in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= x < R and 0 <= y < C and grid[x][y]== 1:
                    dfs(x, y)
        
        for r in range(R):
            for c in range(C):
                # if the land is surrounded by the boudary
                if grid[r][c] == 1 and (r == 0 or c == 0 or r == R - 1 or c == C - 1):
                    dfs(r, c)
        return sum(sum(row) for row in grid)
