class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        idx = -1
        count = 0
        N = len(nums)

        for i in range(N-1):
            if nums[i] >= nums[i + 1]:
                idx = i
                count += 1
        
        if count == 0:
            return True
        
        if count == 1:
            if idx == 0 or idx == N-2:
                return True
            # remove itself? or remove the next one?
            if nums[idx-1] < nums[idx+1] or (idx+2 < N and nums[idx] < nums[idx+2]):
                return True

        return False
