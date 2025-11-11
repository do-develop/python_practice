class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        @cache
        def dp(col, val):
            if col == len(grid[0]):
                return 0
            
            count = 0
            for r in range(len(grid)):
                if grid[r][col] != val:
                    count += 1

            ans = float('inf')

            for k in range(10):
                if k == val:
                    continue
                ans = min(ans, count + dp(col + 1, k))
            return ans

        return min(dp(0, v) for v in range(10))