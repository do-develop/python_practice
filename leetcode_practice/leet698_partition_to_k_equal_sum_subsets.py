"""
Given an integer array nums and an integer k, return true if it is possible to
divide this array into k non-empty subsets whose sums are all equal.
"""
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) / k
        used = [False] * len(nums)

        def backtrack(i: int, k: int, subsetSum: float):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k-1, 0)

            for idx in range(i, len(nums)):
                if used[idx] or subsetSum + nums[idx] > target:
                   continue
                
                used[idx] = True
                if backtrack(idx+1, k, subsetSum + nums[idx]):
                    return True
                used[idx] = False
                
        return backtrack(0, k, 0)
        



# TEST
nums = [4,3,2,3,5,2,1]
k = 4
print(Solution().canPartitionKSubsets(nums, k))
"""
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3),
(2,3) with equal sums.
"""
