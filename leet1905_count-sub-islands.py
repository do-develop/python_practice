class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid2), len(grid2[0])
        
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols and grid2[r][c]==1):
                return 1
            grid2[r][c] = 0
            res = grid1[r][c]
            for dr, dc in [[0,1], [1,0], [-1,0], [0,-1]]:
                res &= dfs(r + dr, c + dc)
            return res

        return sum(dfs(r, c) for r in range(rows) for c in range(cols) if grid2[r][c])
