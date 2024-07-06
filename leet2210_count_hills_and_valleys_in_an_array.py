class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        N = len(nums)
        counter = 0
        left = 0

        for i in range(1, N - 1):
            if (nums[left] < nums[i] and nums[i + 1] < nums[i]) or \
            (nums[left] > nums[i] and nums[i + 1] > nums[i]):
                counter += 1
                left = i
        
        return counter
