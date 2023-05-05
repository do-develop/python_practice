class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n

        for i in range(k):
            dp[i] = max(arr[:i + 1]) * (i + 1)

        for idx in range(k, n):
            curr = []
            for sidx in range(k):
                curr.append(dp[idx - sidx - 1] + max(arr[idx-sidx : idx+1]) * (sidx + 1))
            dp[idx] = max(curr)
        
        return dp[-1]
