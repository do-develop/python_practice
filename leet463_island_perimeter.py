class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col, perim = len(grid), len(grid[0]), 0
        
        for r in range(row):
            for c in range(col):
                perim += 4 * grid[r][c]
                # remove the jointed side
                if r > 0:       perim -= grid[r][c] * grid[r-1][c]
                if r < row-1:   perim -= grid[r][c] * grid[r+1][c]
                if c > 0:       perim -= grid[r][c] * grid[r][c-1]
                if c < col-1:   perim -= grid[r][c] * grid[r][c+1]
        
        return perim
