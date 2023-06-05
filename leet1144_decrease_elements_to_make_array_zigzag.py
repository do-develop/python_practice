class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        nums = [float('inf')] + nums + [float('inf')]
        res = [0, 0] # even or odd
        for i in range(1, len(nums) - 1):
            # max function to ignore the case where no moves needed
            res[i % 2] += max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
        return min(res)
