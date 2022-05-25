"""
Given an array nums of n integers where nums[i] is in the range [1, n], return
an array of all the integers in the range [1, n] that do not appear in nums.
"""
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # mark existing
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        result = []
        for i, n in enumerate(nums):
            if n > 0:
                result.append(i + 1)
        return result



# TEST
nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))
# Output: [5,6]
