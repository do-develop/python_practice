"""
The frequency of an element is the number of times it occurs in an array.
You are given an integer array nums and an integer k. In one operation, you can choose an index 
of nums and increment the element at that index by 1. Return the maximum possible frequency 
of an element after performing at most k operations.
"""


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        l, r = 0, 0
        result, total = 0, 0

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r - l + 1) > total + k:  # invalid
                total -= nums[l]
                l += 1

            result = max(result, r -l +1)
            r += 1

        return result




# TEST
nums = [1,2,4]
k = 5
print(Solution().maxFrequency(nums, k))
# expected output: 3
