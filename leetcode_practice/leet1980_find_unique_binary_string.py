"""
Given an array of strings nums containing n unique binary strings each of
length n, return a binary string of length n that does not appear in nums.
If there are multiple answers, you may return any of them.
"""
from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""
        for i in range(len(nums)):
            if nums[i][i] == '0':
                ans += '1'
            else:
                ans += '0'
        return ans





# TEST
nums = ["111","011","001"]
print(Solution().findDifferentBinaryString(nums))
"""
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110"
would also be correct.
"""
