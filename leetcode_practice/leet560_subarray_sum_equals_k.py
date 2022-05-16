"""
Given an array of integers nums and an integer k, return the total number of
continuous subarrays whose sum equals to k.
"""
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        cur_sum = 0
        prefix_sum = {0:1}

        for n in nums:
            cur_sum += n
            diff = cur_sum - k

            result += prefix_sum.get(diff, 0)
            prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0)

        return result




# TEST
nums = [1,2,3]
k = 3
print(Solution().subarraySum(nums, k))
# expected output: 2
