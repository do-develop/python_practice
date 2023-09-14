class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(pos, parent):
            if pos in visited: return True
            visited.add(pos)
            x, y = pos
            neighbors = []
            new_dirs = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
            for nx, ny in new_dirs:
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == grid[x][y] and (nx, ny) != parent:
                    neighbors.append((nx, ny))
            for nei in neighbors:
                if dfs(nei, pos):
                    return True
            return False

        rows, cols = len(grid), len(grid[0])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited:
                    continue
                if dfs((r, c), None):
                    return True
        return False
        
