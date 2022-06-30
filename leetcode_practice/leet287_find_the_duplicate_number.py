"""
Given an array of integers nums containing n + 1 integers where each integer
is in the range [1, n] inclusive. There is only one repeated number in nums,
return this repeated number. You must solve the problem without modifying the
array nums and uses only constant extra space.
"""
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # phase 1 - find the intersection
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # phase 2 - find the beginning of a cycle
        slow2 = 0
        while True:
            slow1 = nums[slow]
            slow2 = nums[slow2]

            if slow1 == slow2:
                break

        return slow1
        
# TEST
nums = [3,1,3,4,2]
print(Solution().findDuplicate(nums))
# expected output: 3
