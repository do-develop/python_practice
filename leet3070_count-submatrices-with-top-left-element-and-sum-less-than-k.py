class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                if r > 0:
                    grid[r][c] += grid[r - 1][c]
                if c > 0:
                    grid[r][c] += grid[r][c - 1]
                if r > 0 and c > 0:
                    grid[r][c] -= grid[r - 1][c - 1]
                

                if grid[r][c] <= k:
                    res += 1
                else:
                    break
        return res
