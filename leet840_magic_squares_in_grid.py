class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for r in range(len(grid)-2):
            for c in range(len(grid)-2):
                temp_grid = [grid[r+k][c:c+3] for k in range(3)]
                if self.isMagicSquare(temp_grid):
                    count += 1
        return count
    
    def isMagicSquare(self, grid):
        flat = [num for row in grid for num in row]
        if sorted(flat) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        
        # now check row, col, diag sums
        row_sums = [sum(row) for row in grid]
        col_sums = [sum([row[i] for row in grid]) for i in range(3)]
        diag_sums = [sum([grid[i][i] for i in range(3)]), (grid[0][2] + grid[1][1] + grid[2][0])]
        row_sums.extend(col_sums)
        row_sums.extend(diag_sums)
   
        return len(set(row_sums)) == 1
