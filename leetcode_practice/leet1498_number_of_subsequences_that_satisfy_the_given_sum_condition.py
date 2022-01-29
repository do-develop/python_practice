"""
You are given an array of integers nums and an integer target.
Return the number of non-empty subsequences of nums such that the sum of the
minimum and maximum element on it is less or equal to target. Since the answer
may be too large, return it modulo 10000000007.
(duplicate is allowed)
"""
from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = (10**9 + 7)

        r = len(nums) - 1
        for i, left in enumerate(nums):
            while (left + nums[r]) > target and i <= r:
                r -= 1
            if i <= r:
                res += (2**(r-i))
                res %= mod

        return res



# Test
nums = [2,3,3,4,6,7]
target = 12
print(Solution().numSubseq(nums, target))  # expected output: 61
