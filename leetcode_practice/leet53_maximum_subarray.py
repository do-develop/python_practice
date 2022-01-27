"""
Given an integer array nums, find the contiguous subarray (containing
at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
"""

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sum = max(max_sum, cur_sum)
        return max_sum

# Test
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))