class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
        dirs = [(left, right), (up, down), (left, down), (right, down), (left, up), (right, up)]    
        def dfs(x:int, y:int) -> bool:
            # base case when it reached the destination
            if x == rows - 1 and y == cols - 1:
                return True
            for (dx, dy) in dirs[grid[x][y] - 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] and (-dx, -dy) in dirs[grid[nx][ny] - 1]:
                    tmp, grid[x][y] = grid[x][y], 0
                    if dfs(nx, ny):
                        return True
                    grid[x][y] = tmp # if we come back to it via backtracking, then restore
            return False
        return dfs(0, 0)
