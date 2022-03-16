"""
The min-product of an array is equal to the minimum value in the array
multiplied by the array's sum. For example, the array [3,2,5] (minimum value
is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.

Given an array of integers nums, return the maximum min-product of any
non-empty subarray of nums. Since the answer may be large, return it modulo
10^9 + 7.

Note that the min-product should be maximized before performing the modulo
operation. Testcases are generated such that the maximum min-product without
modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.
"""
from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        result = 0
        stack = []
        prefix = [0]

        for n in nums:
            prefix.append(prefix[-1] + n)

        for i, n in enumerate(nums):
            new_start = i
            while stack and stack[-1][1] > n:
                start, val = stack.pop()
                total = prefix[i] - prefix[start]
                result = max(result, val * total)
                new_start = start
                
            stack.append((new_start, n))

        for start, val in stack:
            total = prefix[len(nums)] - prefix[start]
            result = max(result, val * total)

        return result % (10**9 + 7)


#TEST
nums = [1,2,3,2]
print(Solution().maxSumMinProduct(nums))
# expected output: 14
