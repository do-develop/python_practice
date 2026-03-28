class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        n = len(strength)
        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == INF:
                continue

            bits = bin(mask).count('1')
            x = 1 + bits * k  # current factor

            # Try adding each unbroken lock next
            for i in range(n):
                if mask & (1 << i):
                    continue
                time = math.ceil(strength[i] / x)
                new_mask = mask | (1 << i)
                dp[new_mask] = min(dp[new_mask], dp[mask] + time)

        return dp[(1 << n) - 1]
