class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Greedy approach
        # if row starts with 0, flip the row
        # if column has more 0 than 1, flip the column

        row, col = len(grid), len(grid[0])
        for r in range(row):
            if grid[r][0] == 0:
                for c in range(col):
                    grid[r][c] ^= 1 # xor with 1
        
        for c in range(col):
            count = sum(grid[r][c] for r in range(row))
            if count < row - count: # has more 0 than 1
                for r in range(row):
                    grid[r][c] ^= 1
        
        return sum(int(''.join(map(str, grid[r])),2) for r in range(row))
