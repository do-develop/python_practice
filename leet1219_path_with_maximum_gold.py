class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [0, 1, 0, -1, 0]

        def dfs(r, c):
            if r < 0 or r == row or c < 0 or c == col or grid[r][c] == 0:
                return 0
            ans = 0
            cur_gold = grid[r][c]
            grid[r][c] = 0
            for i in range(4):
                ans = max(ans, dfs(r + directions[i], c + directions[i + 1]))
            grid[r][c] = cur_gold
            return ans + grid[r][c]

        ans = 0
        for r in range(row):
            for c in range(col):
                ans = max(ans, dfs(r, c))
        return ans
