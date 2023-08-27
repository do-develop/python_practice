class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = longest = start = 0

        for i in range(len(nums)):
            zeros += (nums[i] == 0)

            while zeros > 1:
                zeros -= (nums[start] == 0)
                start += 1
            
            longest = max(longest, i - start)
        return longest
