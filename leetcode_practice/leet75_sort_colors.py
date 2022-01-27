"""
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red,
white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""
from typing import List

# Quick Sort Approach
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        mid = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while mid <= right:
            if nums[mid] == 0:
                swap(left, mid)
                left += 1
            elif nums[mid] == 2:
                swap(mid, right)
                right -= 1
                mid -= 1  # to cancel out the mid increment
            mid += 1




# Test
nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)
print(nums)