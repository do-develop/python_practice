class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # DP approach
        N = len(nums)

        @lru_cache(6000)
        def dp(l: int, r: int, target: int) -> int:
            if r - l < 2:
                return (r - l == 1 and nums[l]+nums[r]== target)
            return max(1 + dp(l + 2, r, target) if nums[l] + nums[l+1] == target else 0,
                        1 + dp(l, r - 2, target) if nums[r] + nums[r-1] == target else 0,
                        1 + dp(l+1, r-1, target) if nums[l] + nums[r] == target else 0)

        return 1 + max(dp(2, N-1, nums[0]+nums[1]),
                        dp(0, N-3, nums[-1]+nums[-2]),
                        dp(1, N-2, nums[0]+nums[-1]))
