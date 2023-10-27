class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        
        def get_sum(left, right):
            return prefix_sum[right + 1] - prefix_sum[left]
        
        @lru_cache(2000)
        def dp(left, right, isAlice):
            if left == right: return 0 # only 1 stone, score is 0

            if isAlice:
                a = dp(left + 1, right, not isAlice) + get_sum(left + 1, right)
                b = dp(left, right - 1, not isAlice) + get_sum(left, right - 1)
                return max(a, b)
            else:
                a = dp(left + 1, right, not isAlice) - get_sum(left + 1, right)
                b = dp(left, right - 1, not isAlice) - get_sum(left, right - 1)
                return min(a, b)
        return dp(0, n - 1, True)
