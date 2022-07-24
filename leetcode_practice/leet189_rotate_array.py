"""
Given an array, rotate the array to the right by k steps, where k is
non-negative.
"""
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        # reverse the whole list
        l, r = 0, len(nums) - 1
        reverse(l, r)

        # reverse the 1st kth part
        l, r = 0, k - 1
        reverse(l, r)

        # rever the kth part to the end of the list
        l, r = k, len(nums) - 1
        reverse(l, r)
            
        

        


# TEST
nums = [-1,-100,3,99]
k = 2
Solution().rotate(nums, k)
print(nums)
"""
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""
