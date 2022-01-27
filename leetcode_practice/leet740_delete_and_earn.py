"""
You are given an integer array nums. You want to maximize the number of points
you get by performing the following operation any number of times:
Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete
every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation
some number of times.
"""
# Dynamic Programming with two variables
from typing import List
import collections

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0, 0
        for i in range(len(nums)):
            cur_earn = nums[i] * count[nums[i]]
            # can't use both cur_earn and earn2
            if i > 0 and nums[i] == nums[i-1] + 1:
                temp = earn2
                earn2 = max(cur_earn + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = cur_earn + earn2
                earn1 = temp
        return earn2


# Test
nums = [2,3,3,5,6,6]
print(Solution().deleteAndEarn(nums))


                
