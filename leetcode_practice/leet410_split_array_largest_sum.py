"""
Given an array nums which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.
"""
from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return subarray + 1 <= m
        
        l, r = max(nums), sum(nums) # smallest result, largest result
        result = r
        while l <= r:
            mid = l + ((r - l) // 2)
            if canSplit(mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result
            
            
        


nums = [7,2,5,10,8]
m = 2
print(Solution().splitArray(nums, m))
"""
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
