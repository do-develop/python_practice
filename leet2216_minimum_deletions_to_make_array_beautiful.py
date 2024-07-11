class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        deleted = 0
        N = len(nums)

        for i in range(N - 1):
            if (i + deleted) % 2 == 0 and nums[i] == nums[i + 1]:
                deleted += 1
        
        return deleted + (N - deleted) % 2
