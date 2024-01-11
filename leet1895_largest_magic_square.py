class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        pref_row = [[0] * (cols + 1) for _ in range(rows)]
        pref_col = [[0] * (rows + 1) for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                pref_row[r][c + 1] = pref_row[r][c] + grid[r][c]
                pref_col[c][r + 1] = pref_col[c][r] + grid[r][c]

        def get_row_sum(row, l, r):
            return pref_row[row][r + 1] - pref_row[row][l]

        def get_col_sum(col, l, r):
            return pref_col[col][r + 1] - pref_col[col][l]

        def check_magic_square(k):
            for r in range(rows - k + 1):
                for c in range(cols - k + 1):
                    diag, antidiag = 0, 0
                    for i in range(k):
                        diag += grid[r + i][c + i]
                        antidiag += grid[r + i][c + k - 1 - i]

                    match = (diag == antidiag)
                    nr, nc = r, c
                    while nr < r + k and match:
                        match = (diag == get_row_sum(nr, c, c + k - 1))
                        nr += 1
                    while nc < c + k and match:
                        match = (diag == get_col_sum(nc, r, r + k - 1))
                        nc += 1
                    if match: return True
            return False
        
        for k in range(min(rows, cols), 1, - 1):
            if check_magic_square(k):
                return k
        return 1
