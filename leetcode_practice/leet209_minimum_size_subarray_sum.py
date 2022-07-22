"""
Given an array of positive integers nums and a positive integer target, return
the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1,
numsr] of which the sum is greater than or equal to target. If there is no
such subarray, return 0 instead.
"""
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        min_len = float("inf")
        
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_len = min((r - l) + 1, min_len)
                total -= nums[l]
                l += 1
        return 0 if min_len == float("inf") else min_len


# TEST
target = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(target, nums))
"""
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""
