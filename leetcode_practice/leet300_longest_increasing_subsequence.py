"""
Given an integer array nums, return the length of the longest strictly
increasing subsequence. A subsequence is a sequence that can be derived
from an array by deleting some or no elements without changing the order
of the remaining elements. For example, [3,6,2,7] is a subsequence of
the array [0,3,1,6,2,2,7].
"""
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    cache[i] = max(cache[i], 1 + cache[j])
        return max(cache)
               

# TEST
nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))
# Expected Output: 4 --> Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
