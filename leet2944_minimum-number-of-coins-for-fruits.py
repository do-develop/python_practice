class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        N = len(prices)
        # dp[i] = minimum cost to collect the first i fruits
        dp = [0] * (N + 1)

        candidates = deque()

        for curr in range(N):
            # Remove candidates that can no longer grant free access to current fruit
            while candidates and (candidates[0] + 1) * 2 < curr + 1:
                candidates.popleft()

            # Maintain only better purchase options
            while candidates and (dp[candidates[-1]] + prices[candidates[-1]] >= dp[curr] + prices[curr]):
                candidates.pop()
            
            # Add current fruit as a potential purchase
            candidates.append(curr)

            # Update min cost
            bestIdx = candidates[0]
            dp[curr + 1] = dp[bestIdx] + prices[bestIdx]
        return dp[-1]
