"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.


# Hash map approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        result, max_count = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if count[n] > max_count:
                result = n
            max_count = max(count[n], max_count)
        return result
        
"""
from typing import List

# Boyer-Moore Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result, count = 0, 0

        for n in nums:
            if count == 0:
                result = n
                
            count += (1 if n==result else -1)

        return result


# Test
nums = [1,2,2,3,3,1,1]
print(Solution().majorityElement(nums))
        
        
