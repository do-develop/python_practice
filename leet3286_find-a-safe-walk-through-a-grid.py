class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        M = len(grid)
        N = len(grid[0])

        visited = [[0 for _ in range(N)] for _ in range(M)]
        memo = {}

        def dfs(x, y, cost):
            if x < 0 or x >= M or y < 0 or y >= N or visited[x][y] == 1 or cost >= health:
                return float('inf')

            if x == M - 1 and y == N - 1:
                return cost + grid[x][y]
            
            if (x, y, cost) in memo:
                return memo[(x, y, cost)]
            
            visited[x][y] = 1

            memo[(x,y,cost)] = min(dfs(x+1,y,cost+grid[x][y]),dfs(x-1,y,cost+grid[x][y]),dfs(x,y+1,cost+grid[x][y]),dfs(x,y-1,cost+grid[x][y]))
            visited[x][y] = 0
            return memo[(x,y,cost)]

        allCost = dfs(0,0,0)
        return allCost < health
