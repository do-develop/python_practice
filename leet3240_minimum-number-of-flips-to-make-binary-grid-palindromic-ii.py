class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        flips = 0
        single = 0 # number of (1, 0) pair
        double = 0 # number of (1, 1) pair

        for r in range(R//2):
            for c in range(C//2):
                ones = grid[r][c] + grid[r][C-1-c] + grid[R-1-r][c] + grid[R-1-r][C-1-c]
                flips += min(ones, 4 - ones)

            if C % 2 == 1:
                ones = grid[r][C//2] + grid[R-1-r][C//2]
                single += (ones == 1)
                double += (ones == 2)

        if R % 2 == 1:
            for c in range(C//2):
                ones = grid[R//2][c] + grid[R//2][C-1-c]
                single += (ones==1)
                double += (ones==2)
            if C % 2 == 1:
                flips += grid[R//2][C//2] # center cell needs to be 0 if it is 1
        
        if double % 2 == 0 or single > 0:
            return flips + single
        
        return flips + 2
