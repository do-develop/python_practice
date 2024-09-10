class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]

        def get_min_path(upRow, col):
            minCost = float('inf')
            for c in range(N):
                cost = dp[upRow][c] + moveCost[grid[upRow][c]][col]
                if cost < minCost:
                    minCost = cost
            return minCost
        
        def dfs(row):
            if row == M:
                return
            for i in range(N):
                if row == 0:
                    dp[row][i] = grid[row][i]
                else:
                    dp[row][i] = get_min_path(row-1, i) + grid[row][i]
            dfs(row + 1)
        
        dfs(0)
        return min(dp[M-1])
                
