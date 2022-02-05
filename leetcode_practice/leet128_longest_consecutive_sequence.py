"""
Given an unsorted array of integers nums, return the length of the longest consecutive
elements sequence. You must write an algorithm that runs in O(n) time.
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1

                longest = max(length, longest)
        return longest
        

# Test
nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums))
