"""
You are given a 0-indexed array nums of distinct integers. You want to
rearrange the elements in the array such that every element in the rearranged
array is not equal to the average of its neighbors. More formally, the
rearranged array should have the property such that for every i in the range
1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

Return any rearrangement of nums that meets the requirements.
"""
from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []

        l, r =0, len(nums)-1
        while len(res) != len(nums):
            res.append(nums[l])
            l += 1

            if l <= r:
                res.append(nums[r])
                r -= 1
        return res



# TEST
nums = [6,2,0,9,7]
print(Solution().rearrangeArray(nums))
# Output: [9,7,6,2,0]
