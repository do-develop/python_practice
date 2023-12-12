class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        count = prev = 0
        for curr in nums:
            if curr <= prev:
                prev += 1
                count += prev - curr
            else:
                prev = curr
        return count
