"""
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


# TEST
nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate(nums))
#Output: true