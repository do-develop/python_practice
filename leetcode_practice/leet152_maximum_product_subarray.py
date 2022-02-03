"""
Given an integer array nums, find a contiguous non-empty subarray within the
array that has the largest product, and return the product. The test cases are
generated so that the answer will fit in a 32-bit integer. A subarray is a
contiguous subsequence of the array. 
"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        cur_max, cur_min = 1, 1
        for n in nums:
            cur_max, cur_min = max(n*cur_max, n*cur_min, n), min(n*cur_max, n*cur_min, n)
            result = max(result, cur_max)
        return result
        

# TEST
nums = [2,3,-2,4]
print(Solution().maxProduct(nums))  # Expected Output: 6

