"""
Given an integer n, break it into the sum of k positive integers, where k >= 2,
and maximize the product of those integers. Return the maximum product you can
get.
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1: 1}

        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num],val)
        return dp[n]
        """
        def dfs(num):
            if num in dp:
                return dp[num]

            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)
            return dp[num]
        
        return dfs(n)
        """
                



# TEST
n = 10
print(Solution().integerBreak(n))
"""
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
"""
