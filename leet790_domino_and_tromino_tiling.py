class Solution:
    def numTilings(self, n: int) -> int:
        # understand patterns and use DP approach
        def solve(i, prev_gap):
            if i > n: # out of bound
                return 0
            if i == n: 
                return not prev_gap # if there is gap, no solution
            if prev_gap:
                return solve(i + 1, False) + solve(i + 1, True)
            return solve(i + 1, False) + solve(i + 2, False) + 2 * solve(i + 2, True)
        return solve(0, False) % 1_000_000_007
