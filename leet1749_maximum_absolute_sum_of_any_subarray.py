class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = mx = mn = 0
        for x in nums:
            mx = max(mx + x, 0)
            mn = min(mn + x, 0)
            ans = max(ans, mx - mn)
        return ans
        
