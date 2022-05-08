"""
Given an integer array nums, return the number of longest increasing
subsequences. Notice that the sequence has to be strictly increasing.
"""
from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {} # key = index, value = [length of LIS, count]
        lenLIS, count = 0, 0

        def dfs(i):
            if i in dp:
                return dp[i]

            maxLen, maxCount = 1, 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:  #make sure increasing order
                    length, count = dfs(j)
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count
            nonlocal lenLIS, count
            if maxLen > lenLIS:
                lenLIS, count = maxLen, maxCnt
            elif maxLen == lenLIS:
                count += maxCnt
            dp[i] = [maxLen, maxCnt]
            return dp[i]

        for i in range(len(nums)):
            dfs(i)

        return count
        




# TEST
nums = [1,3,5,4,7]
print(Solution().findNumberOfLIS(nums))
"""
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and
[1, 3, 5, 7]
"""
