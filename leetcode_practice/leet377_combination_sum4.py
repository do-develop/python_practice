"""
Given an array of distinct integers nums and a target integer target, return
the number of possible combinations that add up to target. The test cases are
generated so that the answer can fit in a 32-bit integer. 
"""
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)

        return dp[target]
        


# TEST
nums = [1,2,3]
target = 4
print(Solution().combinationSum4(nums, target))
# expected output: 7
