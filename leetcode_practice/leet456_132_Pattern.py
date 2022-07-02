"""
Given an array of n integers nums, a 132 pattern is a subsequence of three
integers nums[i], nums[j] and nums[k] such that i < j < k and
nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
"""
from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # pair [num, minLeft], monotonically decreasing
        curMin = nums[0]

        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n > stack[-1][1]:
                return True

            stack.append([n, curMin])
            curMin = min(curMin, n)

        return False
        



nums = [-1,3,2,0]
print(Solution().find132pattern(nums))
"""
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2],
[-1, 3, 0] and [-1, 2, 0].
"""
