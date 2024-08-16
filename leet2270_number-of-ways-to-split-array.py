class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        N = len(nums)
        total = sum(nums)
        left = 0
        ways = 0

        for i in range(N - 1):
            left += nums[i]
            right = total - left
            if left >= right:
                ways += 1
        return ways
