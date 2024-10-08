class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [1] + [0] * (n - 1)
        share = 0

        for i in range(1, n):
            share = (share + dp[i - delay] - dp[i - forget]) % mod
            dp[i] = share
        return sum(dp[-forget:]) % mod
