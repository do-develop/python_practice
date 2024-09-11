class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        N = len(grid)
        i, j, k = 0, 0, N - 1

        while i in range(N) and j in range(N):
            if grid[i][j] == 0:
                return False
            if grid[k][j] == 0:
                return False
            grid[i][j] = 0
            grid[k][j] = 0
            i += 1 # primary diagonal
            j += 1 # common column factor
            k -= 1 # secondary diagonal

        check = 0
        for r in range(N):
            for c in range(N):
                check += grid[r][c]

        return False if check > 0 else True
