class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        # interchange rows and columns
        transposed_grid = zip(*grid)

        # vertical & horizontal skylines
        vertical = [max(row) for row in grid]               # seen from east/west
        horizontal = [max(row) for row in transposed_grid]  # seen from north/south

        res = 0
        for r in range(ROW):
            for c in range(COL):
                diff = min(horizontal[c], vertical[r]) - grid[r][c]
                res += diff
        return res
