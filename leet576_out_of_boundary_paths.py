class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[-1] * (maxMove + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        def solve(r, c, maxMove):
            if maxMove < 0:
                return 0
            if r < 0 or c < 0 or r >= m or c >= n:
                return 1
            if dp[r][c][maxMove] != -1:
                return dp[r][c][maxMove]
            
            dp[r][c][maxMove] = (
                solve(r - 1, c, maxMove - 1) +
                solve(r + 1, c, maxMove - 1) + 
                solve(r, c + 1, maxMove - 1) +
                solve(r, c - 1, maxMove - 1)
            )
            return dp[r][c][maxMove]
        return solve(startRow, startColumn, maxMove) % 1000000007
