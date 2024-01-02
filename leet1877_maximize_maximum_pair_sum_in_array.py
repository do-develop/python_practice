class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        for i in range(len(nums) // 2):
            pair_sum = nums[i] + nums[len(nums) - i - 1]
            max_sum = max(max_sum, pair_sum)
        return max_sum
