"""
Given a non-empty array nums containing only positive integers, find if the
array can be partitioned into two subsets such that the sum of elements in
both subsets is equal.
"""
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)):
            new_dp = set()
            for t in dp:
                if nums[i] + t == target:
                    return True
                new_dp.add(nums[i] + t)
                new_dp.add(t)
            dp = new_dp

        return True if target in dp else False 




# TEST
nums = [1,5,11,5]
print(Solution().canPartition(nums))
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
