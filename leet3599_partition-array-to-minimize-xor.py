class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        N = len(nums)
        prefix = [0] * (N + 1)

        # step 1: prefix XOR
        for i in range(1, N + 1):
            prefix[i] = prefix[i - 1] ^ nums[i - 1]

        # step 2: DP table
        dp = [[float('inf')] * (k + 1) for _ in range (N + 1)]
        for i in range(N + 1):
            dp[i][1] = prefix[i] # base

        # step 3: perform XOR
        for part in range (2, k + 1):
            for end in range(part, N + 1):
                for start in range(part - 1, end):
                    curXOR = prefix[end] ^ prefix[start]
                    maxXOR = max(dp[start][part - 1], curXOR)
                    dp[end][part] = min(dp[end][part], maxXOR)
        
        return dp[N][k]
