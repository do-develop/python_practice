class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        # DP approach
        INF = float('inf')
        # return minimum waste from i with k operations
        @cache
        def dp(i, k):
            if i == len(nums): return 0
            if k < 0: return INF
            ans = INF
            max_n = nums[i]
            total = 0
            for j in range(i, len(nums)):
                max_n = max(max_n, nums[j])
                total += nums[j]
                wasted = max_n * (j - i + 1) - total
                ans = min(ans, dp(j + 1, k - 1) + wasted)
            return ans
        return dp(0, k)
