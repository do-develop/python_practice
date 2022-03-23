"""
There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges n is divisible by 2 then you can eat n / 2 oranges.
If the number of remaining oranges n is divisible by 3 then you can eat 2 * (n / 3) oranges.
You can only choose one of the actions per day.

Given the integer n, return the minimum number of days to eat n oranges.
"""

class Solution:
    def minDays(self, n: int) -> int:
        dp = {0:0, 1:1}

        def dfs(n):
            if n in dp:
                return dp[n]

            case1 = 1 + (n % 2) + dfs(n // 2)
            case2 = 1 + (n % 3) + dfs(n // 3)
            dp[n] = min(case1, case2)
            return dp[n]
        return dfs(n)
        



# TEST
n = 10
print(Solution().minDays(n))
# expected output: 4
