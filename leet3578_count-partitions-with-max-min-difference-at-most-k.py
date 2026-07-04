class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        N = len(nums)
        mod = 10**9 + 7
        dp = [0] * (N + 1)
        # running sum of dp
        prefix = [0] * (N + 1)
        cnt = SortedList()

        dp[0] = 1
        prefix[0] = 1

        # the smallest starting index such that the window nums[j..i]
        # still satisfies max - min <= k
        j = 0
        for i in range(N):
            cnt.add(nums[i])
            while j <= i and cnt[-1] - cnt[0] > k:
                cnt.remove(nums[j])
                j += 1
            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % mod
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod
        return dp[N]
