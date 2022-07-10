"""
Given an array nums containing n distinct numbers in the range [0, n], return
the only number in the range that is missing from the array.
"""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])

        return res
        



nums = [3,0,1]
print(Solution().missingNumber(nums))
"""
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range
[0,3]. 2 is the missing number in the range since it does not appear in nums.
"""
