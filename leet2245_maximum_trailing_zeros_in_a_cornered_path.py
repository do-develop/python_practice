class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        left = [[[0,0] for _ in range(COL)] for _ in range(ROW)]
        top = [[[0,0] for _ in range(COL)] for _ in range(ROW)]

        def helper(num):
            exp2, exp5 = 0, 0
            while num % 2 == 0:
                num //= 2
                exp2 += 1
            while num % 5 == 0:
                num //= 5
                exp5 += 1
            return [exp2, exp5]
        
        for r in range(ROW):
            for c in range(COL):
                if c == 0:
                    left[r][c] = helper(grid[r][c])
                else:
                    ep2, ep5 = helper(grid[r][c])
                    left[r][c][0] = left[r][c - 1][0] + ep2
                    left[r][c][1] = left[r][c - 1][1] + ep5

        for c in range(COL):
            for r in range(ROW):
                if r == 0:
                    top[r][c] = helper(grid[r][c])
                else:
                    ep2, ep5 = helper(grid[r][c])
                    top[r][c][0] = top[r - 1][c][0] + ep2
                    top[r][c][1] = top[r - 1][c][1] + ep5

        ans = 0
        for r in range(ROW):
            for c in range(COL):
                B2, B5 = top[ROW - 1][c]
                R2, R5 = left[r][COL - 1]
                x, y = helper(grid[r][c]) # center
                T2, T5 = top[r][c]
                L2, L5 = left[r][c]
                tmp = [T2 + L2 - x, T5 + L5 - y]
                ans = max(ans, min(tmp))
                tmp = [R2 - L2 + T2, R5 - L5 + T5]
                ans = max(ans, min(tmp))
                tmp = [B2 - T2 + L2, B5 - T5 + L5]
                ans = max(ans, min(tmp))
                tmp = [B2 + R2 - L2  - T2 + x, B5 + R5 - L5 - T5 + y]
                ans = max(ans, min(tmp))
        return ans
