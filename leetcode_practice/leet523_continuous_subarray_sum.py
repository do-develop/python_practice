"""
Given an integer array nums and an integer k, return true if nums has a
continuous subarray of size at least two whose elements sum up to a multiple
of k, or false otherwise. An integer x is a multiple of k if there exists an
integer n such that x = n * k. 0 is always a multiple of k.
"""
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1} # map remainder -> end index
        total = 0

        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False


# TEST
nums = [23,2,6,4,7]
k = 6
print(Solution().checkSubarraySum(nums, k))
"""
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements
sum up to 42. 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
"""
