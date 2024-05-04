class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [1] * N
        for i in range(1, N):
            if prices[i] == prices[i - 1] - 1:
                dp[i] += dp[i - 1]
        return sum(dp)
