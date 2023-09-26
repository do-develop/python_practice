class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        rows, cols = len(grid), len(grid[0])
        maxp = [[0] * cols for _ in range(rows)]
        minp = [[0] * cols for _ in range(rows)]
        maxp[0][0] = grid[0][0]
        minp[0][0] = grid[0][0]

        for r in range(1, rows):
            maxp[r][0] = maxp[r-1][0] * grid[r][0]
            minp[r][0] = minp[r-1][0] * grid[r][0]

        for c in range(1, cols):
            maxp[0][c] = maxp[0][c-1] * grid[0][c]
            minp[0][c] = minp[0][c-1] * grid[0][c]

        for r in range(1, rows):
            for c in range(1, cols):
                if grid[r][c] > 0:
                    maxp[r][c] = max(maxp[r-1][c], maxp[r][c-1]) * grid[r][c]
                    minp[r][c] = min(minp[r-1][c], minp[r][c-1]) * grid[r][c]
                else:
                    maxp[r][c] = min(minp[r-1][c], minp[r][c-1]) * grid[r][c]
                    minp[r][c] = max(maxp[r-1][c], maxp[r][c-1]) * grid[r][c]
        return maxp[-1][-1] % mod if maxp[-1][-1] >= 0 else -1
