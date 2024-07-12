class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        N = len(nums)
        start, end = 0, N - 1
        while start < end:
            for i in range(start, end):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            end -= 1
        
        return nums[0]
