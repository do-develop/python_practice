class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        N = len(nums)

        ones_in_window, count_one = 0, 0
        for i in range(N * 2):
            if i >= ones and nums[i % N - ones]: # left most
                count_one -= 1
            if nums[i % N] == 1: # right most
                count_one += 1

            ones_in_window = max(count_one, ones_in_window)
        
        return ones - ones_in_window
