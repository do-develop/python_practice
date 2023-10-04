class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        @lru_cache(None)
        def dp(i, k, start_here):
            if k == 0: return 1 # Found a way to draw k valid segments
            if i == n: return 0 # Reached the end of points
            ans = dp(i + 1, k, start_here) # skip ith point
            if start_here: # take ith point as start
                ans += dp(i + 1, k, False) 
            else: # take ith point as end
                ans += dp(i, k - 1, True) 
            return ans % mod

        return dp(0, k, True)
