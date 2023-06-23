class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # instead of nested loop by using dp, the time complexity in O(n)
        dp = {}
        answer = 1
        for n in arr:
            n_before = dp.get(n - difference, 0)
            dp[n] = n_before + 1
            answer = max(answer, dp[n])
        return answer
