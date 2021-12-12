"""
Given a non-empty array of integers nums, every element appears
twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity
and use only constant extra space.


# Method 1 - Counter()
from typing import List
import collections

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt_dict = collections.Counter(nums)
        items = cnt_dict.items()

        for key, val in items:
            if val == 1:
                answer = key
                break

        return answer

"""

from typing import List
import collections

# Method 2 - bit calculation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in nums:
            answer ^= i
        return answer


# Test
nums = [3,1,2,1,2]
print(Solution().singleNumber(nums))
