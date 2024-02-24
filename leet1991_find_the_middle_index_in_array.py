class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        for idx in range(len(nums)):
            if sum(nums[:idx]) == sum(nums[idx + 1:]):
                return idx
        return -1
